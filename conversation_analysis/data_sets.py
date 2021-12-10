# Datasources:
#
# http://convai.io/2017/data/
#       http://convai.io/2017/data/train_full.json
#       http://convai.io/2017/data/Dataset_Analysis.ipynb
#       http://convai.io/2017/data/dataset_description.pdf
#
# https://www.amazon.science/blog/amazon-releases-data-set-of-annotated-conversations-to-aid-development-of-socialbots
#       https://assets.amazon.science/04/10/200f21ec448e95274536eb969f8c/topical-chat-towards-knowledge-grounded-open-domain-conversations.pdf
#
# https://ml.christmas/2019/15
#
# https://hackernoon.com/top-15-chatbot-datasets-for-nlp-projects-8k2f3zqc
#
# https://www.kaggle.com/shuyangli94/interview-npr-media-dialog-transcripts
#

'''
This module builds pytorch Datasets and provides an appropriate collate function so that the
Dataset can be put into a Dataloader.

The pad_collate function below is a small modification of Suzanna Sia's function found at:
https://suzyahyah.github.io/pytorch/2019/07/01/DataLoader-Pad-Pack-Sequence.html
'''

from nltk import tokenize
from gingerit.gingerit import GingerIt
import requests
import json
from torch.utils.data import Dataset, DataLoader, Subset
import torch
from torch.nn.utils.rnn import pad_sequence
from sklearn.model_selection import train_test_split, StratifiedKFold

import dialog2tensor


class DoNothingParser:
    def __init__(self):
        pass

    def parse(self, s):
        return {'result': s}


class ConvoAI3Data:
    def __init__(self, parser):
        self.parser = parser
        url = 'http://convai.io/2017/data/train_full.json'
        r = requests.get(url)
        self.conversation_list = json.loads(r.content)

    def label_and_clean_dialog(self, c):
        label_dict = {u['id']: u['userType'] for u in c['users']}
        dialog = []
        for t in c['thread']:
            speaker = t['userId']
            text = t['text']
            sentences = tokenize.sent_tokenize(text)
            parsed = [self.parser.parse(sentence)['result'] for sentence in sentences]
            dialog.extend([(speaker, g) for g in parsed])
        return label_dict, dialog


class ConvoAI3AsTensorDataset(Dataset):
    def __init__(self, convo_ai3_data, dialog_encoder):
        super().__init__()
        self.raw_data = convo_ai3_data

        clean_labeled_convos = [convo_ai3_data.label_and_clean_dialog(c) for c in convo_ai3_data.conversation_list]

        self.raw_labels = [lc[0] for lc in clean_labeled_convos]
        labels = [(l['Alice'] == 'Bot', l['Bob'] == 'Bot') for l in self.raw_labels]
        labels = [l[0] + l[1] * 2 for l in labels]  # alice == bot is label % 2, bob == bot is label // 4
        eye = torch.eye(4)
        self.label_tensor = eye[labels]  # one-hot encoding trick

        clean_convos = [lc[1] for lc in clean_labeled_convos]
        self.dialog_tensor_list = []  # [dialog_encoder.encode_dialog(c) for c in clean_convos]

        print(f"Beginning processing {len(labels)} dialogs.")
        for i, c in enumerate(clean_convos):
            print(f"Processing {i + 1}th dialog.", end='\r')
            self.dialog_tensor_list.append(dialog_encoder.encode_dialog(c))
        print("")
        print("Dialog processing complete.")

    def __len__(self):
        return len(self.label_tensor)

    def __getitem__(self, index):
        return (self.dialog_tensor_list[index], self.label_tensor[index])


def train_validate_test_datasets(dataset, train_size=None, test_size=None, n_splits=1, random_state=None):
    train_size = train_size if train_size else 1 - test_size
    test_size = test_size if test_size else 1 - train_size

    y = dataset.label_tensor
    X = list(range(len(y)))
    full_train_idxs, test_idxs, _, _ = train_test_split(X, y, train_size=train_size, test_size=test_size,
                                                        shuffle=True, stratify=y, random_state=random_state)
    full_train_dataset = Subset(dataset, full_train_idxs)
    full_train_dataset.label_tensor = y[full_train_idxs]
    test_dataset = Subset(dataset, test_idxs)
    test_dataset.label_tensor = y[test_idxs]

    y = full_train_dataset.label_tensor
    X = torch.zeros(len(y))
    if n_splits > 1:
        tv_skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=random_state)
        splits = tv_skf.split(X, y.argmax(dim=1))  # returns iterable of (train_idxs, validate_idxs) tuples
    else:
        train_idxs, validate_idxs, _, _ = train_test_split(X, y, train_size=train_size, test_size=test_size,
                                                           stratify=y, shuffle=True, random_state=random_state)
        splits = [(train_idxs, validate_idxs)]

    train_val_gen = ((Subset(full_train_dataset, s[0]), Subset(full_train_dataset, s[1])) for s in splits)

    return full_train_dataset, train_val_gen, test_dataset


def pad_collate(batch):
    (dialogs, labels) = zip(*batch)
    dialog_lengths = [len(s) - 2 for s in dialogs]  # SoD and EoD tokens are subtracted off.

    dialogs_tensor = pad_sequence(dialogs)
    labels_tensor = torch.stack(labels)

    return dialogs_tensor, labels_tensor, dialog_lengths


if __name__ == "__main__":
    import random

    cai3data = ConvoAI3Data(parser=DoNothingParser())

    d = random.choice(cai3data.conversation_list)
    print(d)

    ln, dn = cai3data.label_and_clean_dialog(d)
    cai3data.parser = GingerIt()
    lg, dg = cai3data.label_and_clean_dialog(d)
    print(ln)
    print(lg)
    for sn, sg in zip(dn[0:3], dg[0:3]):
        print(sn)
        print(sg)

    from sentence_transformers import SentenceTransformer

    cai3data.parser = DoNothingParser()

    sentence_encoder = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    sentence_dimension = sentence_encoder.encode("").shape[0]
    positional_encoder = dialog2tensor.PositionalEncoding(dimension=1 + sentence_dimension, max_position=100)
    dia_enc = dialog2tensor.DialogEncoder(sentence_encoder.encode, positional_encoder)
    cai3dataset = ConvoAI3AsTensorDataset(cai3data, dia_enc)

    ####

    cai3dataloader = DataLoader(cai3dataset, batch_size=2, collate_fn=pad_collate)

    st, lt, s_lens = next(iter(cai3dataloader))
    print(f"st.shape = {st.shape}")
    print(f"lt.shape = {lt.shape}")
    print(f"s_lens length = {len(s_lens)}")

    ####

 #   from sklearn.model_selection import StratifiedKFold, train_test_split
    import random

    y = cai3dataset.label_tensor
    X = list(range(len(y)))
    train_idxs, test_idxs, _, _ = train_test_split(X, y, train_size=0.9, stratify=y)

    #from torch.utils.data import Subset

    train_set = Subset(cai3dataset, train_idxs)
    test_set = Subset(cai3dataset, test_idxs)

    train_set.label_tensor = cai3dataset.label_tensor[train_idxs]

    tv_skf = StratifiedKFold(n_splits=3)
    y = train_set.label_tensor
    X = torch.zeros(len(y))
    splits = tv_skf.split(X, y.argmax(dim=1))  # returns iterable of (train_indexes, validate_indexes) tuples

    split = next(splits)

    ktrain_set = Subset(cai3dataset, split[0])
    kvalidate_set = Subset(cai3dataset, split[1])

    batch_size = 10
    shuffle = True

    train_loader = DataLoader(ktrain_set, batch_size=batch_size, shuffle=False, collate_fn=pad_collate)
    validate_loader = DataLoader(kvalidate_set, batch_size=batch_size, shuffle=False, collate_fn=pad_collate)

    for x, y, dialog_lengths in train_loader:
        print(x.shape, y.shape, dialog_lengths)

    full, tvgen, tst = train_validate_test_datasets(cai3dataset, test_size=0.1, n_splits=3, random_state=4)
