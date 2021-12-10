import torch
import torch.nn as nn
from torch.nn.utils.rnn import pad_sequence
import random


class TransformerEncoderMulticlass(nn.Module):
    def __init__(self, num_layers, num_features, num_heads, num_classes, dropout=0.1):
        super().__init__()

        self.num_layers = num_layers
        self.num_features = num_features
        self.num_heads = num_heads
        self.num_classes = num_classes
        self.dropout = dropout

        encoder_layer = nn.TransformerEncoderLayer(d_model=num_features, nhead=num_heads, dropout=dropout)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)

        self.to_classes = nn.Sequential(
            nn.Flatten(),
            nn.Linear(num_features, num_classes),
            nn.ReLU(),
        )

    def forward(self, x):
        te = self.transformer_encoder(x)
        return self.to_classes(te[0])

    def __str__(self):
        return f"TransEnc{self.num_layers}.{self.num_features}.{self.num_heads}.{self.num_classes}.{self.dropout}"

if __name__ == "__main__":
    num_features = 100
    input_tensor_list = [torch.rand((random.randint(1, 20), 100)) for _ in range(10)]
    print([t.shape[0] for t in input_tensor_list])
    input_tensor = pad_sequence(input_tensor_list)
    print(f"input_tensor.shape = {input_tensor.shape}")

    tem = TransformerEncoderMulticlass(4, 100, 2, 4)
    output = tem(input_tensor)
    print(output.shape)
