import torch
from tokenizer import Tokenizer


text = open("../data/input.txt", encoding="utf-8").read()
unique_chars = sorted(set(text)) # do sorting own logic

Tokenizer = Tokenizer(text)
data = torch.tensor(Tokenizer.encode(text), dtype=torch.long)
print(data)
print(Tokenizer.decode(data.tolist()))

n = int(0.9 * len(data))

train_data = data[:n]
val_data = data[n:]

class Train:
    def __init__(self) -> None:
        pass

