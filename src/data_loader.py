# this should load the data in chunks and map all unique characters
from collections.abc import Iterator
from tokenizer import Tokenizer
import torch
import numpy as np

class Data_Loader:
    def read_chunks(self, file_path : str, chunk_size : int = 64 * 1024) -> Iterator[str]:
        with open(file_path, encoding="utf-8") as file:
            while chunk := file.read(chunk_size):
                yield chunk

    def text_to_tensor(self, text : str, token_ids : list[int], tokenizer : Tokenizer) -> torch.tensor:
        data : torch.tensor = torch.tensor(token_ids, dtype=torch.long)
        return data 

    def preprocess(self, file_path : str, file_size : int, tokenizer : Tokenizer, chunk_size : int = 10_000, train_ratio : float = 0.9) -> tuple[str, str]:
        token_ids : list[int] = tokenizer.encode(text)

        last_train_index : int = int(file_size * train_ratio)
        first_val_index : int = file_size - last_train_index

        if last_train_index <= 0 or first_val_index <= 0:
            raise ValueError("Both splits must contain data.")

        train_path = "../data/train.txt"
        val_path = "../data/val.txt"

        train_ids = np.lib.format.open_memmap(
            train_path, mode="w+", dtype=np.int64, shape=(last_train_index,)
        )

        val_ids = np.lib.format.open_memmap(
            val_path, mode="w+", dtype=np.int64, shape=(first_val_index,)
        )


        train_pos : int = 0
        val_pos : int = 0
        for chunk in self.read_chunks(file_path, chunk_size):

            token_ids : list[int] = tokenizer.encode(chunk)

            remaining_train : int = last_train_index - train_pos
            train_data = min(len(token_ids), remaining_train) # make sure to only take train_ratio of the data for training

            train_part = token_ids[:train_data]
            val_part = token_ids[train_data:]

            train_end = train_pos + len(train_part)
            train_ids[train_pos:train_end] = train_part
            train_pos = train_end

            val_end = val_pos + len(val_part)
            val_ids[val_pos:val_end] = val_part
            val_pos = val_end

        if train_pos != last_train_index or val_pos != first_val_index:
            raise ValueError("The text length differs from the first pass.")

        train_ids.flush()
        val_ids.flush()

        return train_path, val_path


    def iter_training_batches(self, file_path : str, chunk_size : int, file_size : int, tokenizer : Tokenizer, split_ratio : list[float] = [0.9, 0.1]) -> Iterator[torch.tensor]:
        #TODO: batch logic, convert into tensor
     
            yield token_tensor

    def iter_validation_batches(self, file_path : str, chunk_size : int, file_size : int, tokenizer : Tokenizer, split_ratio : list[float] = [0.9, 0.1]) -> Iterator[torch.tensor]:


        # chunk up to 90% line should stream into model.train
        # chunk after 90 should then --------||---model.val
        #TODO: stream as validation data into model in last stages

        for 




if __name__ == "__main__":

    txt_dir = "../data/input.txt"
    text = open(txt_dir, encoding="utf-8").read() # change to read biger files

    tk = Tokenizer(text)

    dl = Data_Loader()
    print(dl.text_to_tensor("hello", tk))
