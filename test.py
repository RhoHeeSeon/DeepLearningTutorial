import torch
import torch.nn as nn


m = nn.LogSoftmax(dim=1)
input = torch.randn(2, 3)
output = m(input)
print(f'input: {input}')
print(f'm: {m}')
print(f'output: {output}')