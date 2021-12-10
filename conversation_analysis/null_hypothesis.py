'''
This module provides a model that simply predicts the most common label amongst all labels.
We call this the null hypothesis because it is the correct model when the labels provide zero information,
i.e. when the null hypothesis is true.
'''

import torch

class NullHypothesis:
    def __init__(self, Y):
        self.return_value = torch.mode(Y)

    def __call__(self, X):
        return self.return_value


if __name__ == "__main__":
    X = torch.rand((5, 3, 7))
    Y = torch.randint(0, 2, (3,))
    nh = NullHypothesis(Y)

    print(Y)
    print(nh(Y))
