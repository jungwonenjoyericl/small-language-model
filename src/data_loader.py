# this should load the data in chunks and map all unique characters
from tokenizer import Tokenizer
import torch

class Data_Loader:
    def __init__(self):
        pass

    def text_to_tensor(self, text : str, tokenizer : Tokenizer) -> torch.tensor:
        token_ids : list[int] = tokenizer.encode(text)
        data : torch.tensor = torch.tensor(token_ids, dtype=torch.long)
        return data


if __name__ == "__main__":

    txt_dir = "../data/input.txt"
    text = open(txt_dir, encoding="utf-8").read() # change to read biger files

    tk = Tokenizer(text)

    dl = Data_Loader()
    print(dl.text_to_tensor("hello", tk))
