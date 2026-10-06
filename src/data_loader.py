# this should load the data in chunks and map all unique characters
from collections.abc import Iterator
from tokenizer import Tokenizer
import torch

class Data_Loader:
    def read_chunks(self, file_path : str, chunk_size : int = 64 * 1024) -> Iterator[str]:
        with open(file_path, encoding="utf-8") as file:
            while chunk := file.read(chunk_size):
                yield chunk

    def text_to_tensor(self, text : str, tokenizer : Tokenizer) -> torch.tensor:
        token_ids : list[int] = tokenizer.encode(text)
        data : torch.tensor = torch.tensor(token_ids, dtype=torch.long)
        return data 

    def iter_training_batches(self, file_path : str, chunk_size : int, file_size : int, split_ratio : list[float] = [0.9]) -> Iterator[torch.tensor]:

        split_border : int = int(file_size * split_ratio)
        cur_text_pos : int = 0
        for chunk in self.read_chunks(file_path, chunk_size): 

            cur_text_pos += len(chunk)
            if cur_text_pos <= split_border:
                #TODO: stream as training data into model
                #model.train
                pass

            else: # chunk up to 90% line should stream into model.train
                  # chunk after 90 should then --------||---model.val
                #TODO: stream as validation data into model in last stages
                
                pass
            


if __name__ == "__main__":

    txt_dir = "../data/input.txt"
    text = open(txt_dir, encoding="utf-8").read() # change to read biger files

    tk = Tokenizer(text)

    dl = Data_Loader()
    print(dl.text_to_tensor("hello", tk))
