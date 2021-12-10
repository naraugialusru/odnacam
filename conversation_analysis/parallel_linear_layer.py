import torch.nn as nn
import torch


class ParallelLinearLayer(nn.Module):

    def __init__(self, input_dim, output_dim):
        super().__init__()
        self.cell = nn.Sequential(nn.Linear(input_dim, output_dim), nn.ReLU())

    def forward(self, X):
        '''
        X has shape (S, N, L), where S is the sequence length, and N is the batch size
        L = input dimension
        '''
        (S, N, L) = X.shape
        X = X.reshape(-1, L)
        Y = self.cell(X)
        Y = Y.reshape(S, N, -1)
        return Y


if __name__ == "__main__":
    X = torch.rand((5, 3, 7))
    Y = torch.randint(0, 2, (3,))
    pll = ParallelLinearLayer(7, 2)

    print(f"Y = {Y}")
    print(f"pll(X).shape = {pll(X).shape}")
