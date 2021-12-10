'''
The classes here are made so that a list of conversations can be converted into a tensor.
This is done by converting sentences into vector a speaker label plus a BERT embedding, putting these
sentence-vectors into a sequence tensor, and then padding all these sequence tensors together
into a big (S, N, L) = (sequence, batch, vector_dim) tensor.

Conversations are lists of (speaker, sentence) pairs. Both speaker and sentence are strings. speaker is either
"Alice" or "Bob". Later, the conversation will be the output of the diarization module.

Each sequence is prepended by a start-of-dialog token and appended by an end-of-dialog token.
The idea is that the start-of-dialog token can be used for classification, like the "class" token used in BERT.
The end-of-dialog token is probably pointless, but it seemed lopsided not to include it.

The positional encoding was taken pretty much directly from the pytorch transformer tutorial:
https://pytorch.org/tutorials/beginner/transformer_tutorial.html
'''

import torch
import torch.nn as nn
from sentence_transformers import SentenceTransformer
from torch.nn.utils.rnn import pad_sequence
import math


class PositionalEncoding(nn.Module):
    def __init__(self, dimension, max_position):
        '''
        The translation_tensor is shape (dimension, 1, max_position). The dimension is 1 + the sentence embedding
        dimension. The +1 entry is encodes the speaker of the dialog. This entry of the vector should not be changed,
        so the translation tensor is 0 in these entries.
        '''
        super().__init__()
        sentence_dimension = dimension - 1
        position = torch.arange(max_position).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, sentence_dimension, 2) * (-math.log(10000.0) / sentence_dimension))

        translation_tensor = torch.zeros((max_position, dimension))
        translation_tensor[:, 1::2] = torch.sin(position * div_term)
        div_term = div_term[:translation_tensor[:, 2::2].shape[1]]  # adjustment for odd sentence_dimension.
        translation_tensor[:, 2::2] = torch.cos(position * div_term)

        self.register_buffer('translation_tensor', translation_tensor)

    def forward(self, x):
        x = x + self.translation_tensor[:x.size(0)]
        return x


class DialogEncoder:
    '''
    This should take N dialogs, pad them to length S, encode them into length L,
    and return a (S, N, L) tensor.

    Note that L is the 1 + the output dimension of the sentence encoder. The extra dimension encodes the speaker.

    Dialogs are assumed to be lists of (speaker, sentence_list) pairs.
    '''

    def __init__(self, sentence_encoder, positional_encoder):
        super().__init__()

        self.sentence_encoder = sentence_encoder
        self.positional_encoder = positional_encoder
        self.sentence_dimension = sentence_encoder("").shape[0]

        start_token = torch.Tensor(self.sentence_encoder('[SoD]'))
        start_token = torch.cat((torch.Tensor([0.5]), start_token), 0)
        start_token = start_token.unsqueeze(0)
        self.start_token = start_token

        end_token = torch.Tensor(self.sentence_encoder('[EoD]'))
        end_token = torch.cat((torch.Tensor([0.5]), end_token), 0)
        end_token = end_token.unsqueeze(0)
        self.end_token = end_token

    def encode_dialog(self, dialog):
        '''
        A dialog is a list of tuples of the form (speaker, sentence).
        Both speaker and sentence are strings.

        Outputs a tensor of the shape (num_sentences+1, L), where L is the encoding dimension.
        The first row (0, *) is a "start token". We are just using all zeros for this.
        '''
        dialog_tensor = torch.Tensor(())
        for speaker, sentence in dialog:
            speaker_id = torch.Tensor([float(speaker != 'Alice')])
            enc_sent = torch.Tensor(self.sentence_encoder(sentence))
            sent = torch.cat((speaker_id, enc_sent), 0)
            dialog_tensor = torch.cat((dialog_tensor, sent.unsqueeze(0)), 0)

        dialog_tensor = torch.cat((self.start_token, dialog_tensor, self.end_token), 0)
        return dialog_tensor

    def encode_batch(self, dialogs):
        enc_dialogs = [self.encode_dialog(dialog) for dialog in dialogs]
        pos_enc_dialogs = [self.positional_encoder(enc_dialog) for enc_dialog in enc_dialogs]
        return pad_sequence(pos_enc_dialogs)


if __name__ == "__main__":
    import data_sets
    import random

    cai3data = data_sets.ConvoAI3Data(parser=data_sets.DoNothingParser())
    sentence_encoder = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    sentence_dimension = sentence_encoder.encode("").shape[0]
    positional_encoder = PositionalEncoding(dimension=1 + sentence_dimension, max_position=100)
    dia_enc = DialogEncoder(sentence_encoder.encode, positional_encoder)

    print("Conversation Throughput:")
    convo = random.choice(cai3data.conversation_list)
    print(f"Random Conversation = {convo}")

    label, clean_convo = cai3data.label_and_clean_dialog(convo)
    print(f"label = {label}")

    dia_tensor = dia_enc.encode_dialog(clean_convo)
    print(f"Dialog Tensor Shape = {dia_tensor.shape}")

    print("\nBatch Throughput:")
    convos = [random.choice(cai3data.conversation_list) for _ in range(5)]
    clean_convos = [cai3data.label_and_clean_dialog(c)[1] for c in convos]
    batch_tensor = dia_enc.encode_batch(clean_convos)

    print(f"Batch Tensor Shape = {batch_tensor.shape}")
    print(f"Batch Tensor Dimension = {batch_tensor.shape[2]}")
