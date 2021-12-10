'''
This module provides a trainer that takes ...
and generates TensorBoard data to compare ...
'''

######

from torch.utils.tensorboard import SummaryWriter

tb = SummaryWriter()

#######


from itertools import product
import torch.nn as nn



#########


from data_sets import ConvoAI3Data, pad_collate, DoNothingParser, ConvoAI3AsTensorDataset, train_validate_test_datasets
from sentence_transformers import SentenceTransformer
import dialog2tensor

cai3data = ConvoAI3Data(parser=DoNothingParser())

sentence_encoder = SentenceTransformer('paraphrase-MiniLM-L6-v2')
sentence_dimension = sentence_encoder.encode("").shape[0]
positional_encoder = dialog2tensor.PositionalEncoding(dimension=1 + sentence_dimension, max_position=100)

dia_enc = dialog2tensor.DialogEncoder(sentence_encoder.encode, positional_encoder)
cai3dataset = ConvoAI3AsTensorDataset(cai3data, dia_enc)

from transformer_encoder_model import TransformerEncoderMulticlass

num_layers = 4
num_features = 1 + sentence_dimension
num_heads = 5
num_classes = 4
dropout = 0.1
model = TransformerEncoderMulticlass(
    num_layers=num_layers,
    num_features=num_features,
    num_heads=num_heads,
    num_classes=num_classes,
    dropout=dropout
)

parameters = {'network': [model], 'lr': [0.01, 0.001], 'batch_size': [100, 1000], 'shuffle': [True, False]}


from torch.utils.data import DataLoader
from torch.optim import Adam

param_values = parameters.values()
grid = list(product(*param_values))

OVERFIT = True

if not OVERFIT:
    N_SPLITS = 10
    full_train_set, train_val_generator, test_set = train_validate_test_datasets(cai3dataset, test_size=0.1,
                                                                                 n_splits=N_SPLITS,
                                                                                 random_state=4)
    MAX_TIME = 60 * 60 * 2  # seconds/min * min/hour * hour
else:
    N_SPLITS = 2
    full_train_set, train_val_generator, _ = train_validate_test_datasets(cai3dataset,
                                                                          test_size=0.9,
                                                                          n_splits=N_SPLITS,
                                                                          random_state=4)
    MAX_TIME = 60 * 30  # seconds/min * min

import copy
import time
import torch

def one_hot_ce_loss(outputs, targets):
    '''
    This function came from beaupreda's contribution to
    https://discuss.pytorch.org/t/loss-function-for-multi-class-with-probabilities-as-output/60866/2

    :param outputs:
    :param targets:
    :return:
    '''
    criterion = nn.CrossEntropyLoss()
    _, labels = torch.max(targets, dim=1)
    return criterion(outputs, labels)

criterion = one_hot_ce_loss

num_passes = N_SPLITS * len(grid)
start_time = time.time() #unused
max_epoch_time = 0

def get_num_correct(preds, labels):
    return preds.argmax(dim=1).eq(labels.argmax(dim=1)).sum().item()

for tv_num, (trn, val) in enumerate(train_val_generator):
    print(f"Split Number = {tv_num}")
    for network, lr, batch_size, shuffle in grid:
        comment = f"network = {str(network)}, lr = {lr}, batch_size = {batch_size}, shuffle={shuffle}, split = {tv_num}"
        print(comment)

        train_loader = DataLoader(trn, batch_size=batch_size, shuffle=shuffle, collate_fn=pad_collate)
        validate_loader = DataLoader(val, batch_size=batch_size, shuffle=False, collate_fn=pad_collate)

        net = copy.deepcopy(network)
        optimizer = Adam(net.parameters(), lr=lr)

        epoch = 0
        pass_start_time = time.time()
        while time.time() - pass_start_time < MAX_TIME / num_passes - max_epoch_time:
            print(f"Epoch = {epoch}")
            epoch_start_time = time.time()
            total_loss = 0
            total_correct = 0
            for i, (x, y, dialog_lengths) in enumerate(train_loader):
                outputs = net(x)
                optimizer.zero_grad()
                loss = criterion(outputs, y)
                loss.backward()
                optimizer.step()
                # record minibatch stats : running_loss += loss.item() etc. -- tensorboard
                minibatch_comment = comment + f", minibatch = {i}"
                print(minibatch_comment)
                total_loss += loss.item() * x.shape[0]
                total_correct += get_num_correct(outputs, y)

            validation_total_loss = 0
            validation_total_correct = 0
            net.eval()
            for x, y, dialog_lengths in validate_loader:
                val_outputs = net(x)
                val_loss = criterion(val_outputs, y)
                validation_total_loss += val_loss
                validation_total_correct += get_num_correct(val_outputs, y)

            print(f"Total Loss = {total_loss}")

            tb.add_scalar(
                comment + ': Loss', total_loss, epoch
            )
            tb.add_scalar(
                comment + ': Number Correct', total_correct, epoch
            )
            tb.add_scalar(
                comment + ': Accuracy', total_correct / len(trn), epoch
            )

            tb.add_scalar(
                comment + f": Validation Loss", validation_total_loss, epoch
            )
            tb.add_scalar(
                comment + f': Validation Number Correct', validation_total_correct, epoch
            )
            tb.add_scalar(
                comment + f': Validation Accuracy', validation_total_correct / len(val), epoch
            )


            for name, weight in net.named_parameters():
                tb.add_histogram(comment + ': ' + name, weight, epoch)
                tb.add_histogram(comment + f': {name}.grad', weight.grad, epoch)

            epoch_end_time = time.time()
            max_epoch_time = max(epoch_start_time - epoch_end_time, max_epoch_time)
            epoch += 1

