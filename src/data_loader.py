# this should load the data in chunks and map all unique characters
from collections.abc import Iterator
from tokenizer import Tokenizer
import torch
import numpy as np

class Data_Loader:
    def read_chunks(self, file_path : str, chunk_size : int = 10_000) -> Iterator[str]:
        with open(file_path, encoding="utf-8") as file:
            while chunk := file.read(chunk_size):
                yield chunk

    def token_ids_to_tensor(self, token_ids : list[list[int]]) -> torch.Tensor:
        data : torch.Tensor = torch.tensor(token_ids, dtype=torch.long)
        return data 

    def preprocess(self, file_path : str, file_size : int, tokenizer : Tokenizer, chunk_size : int = 10_000, train_ratio : float = 0.9) -> tuple[str, str]:

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


    def iter_batches(self, file_path : str, sequence_length : int, batch_size : int) -> Iterator[tuple[torch.Tensor, torch.Tensor]]:

        if sequence_length <= 0 or batch_size <= 0:
            raise ValueError("Sequence length and batch size must be positive")

        token_ids = np.load(file_path, mmap_mode="r")
        current_index = 0

        while current_index + sequence_length < len(token_ids):
            input_rows = []
            output_rows = []

            for _ in range(batch_size):
                if current_index + sequence_length >= len(token_ids):
                    break

                input_sequence : list[int] = token_ids[current_index : current_index + sequence_length].tolist()
                
                target_index = current_index + 1
                target_sequence : list[int] = token_ids[target_index : target_index + sequence_length].tolist()
                
                input_rows.append(input_sequence)
                output_rows.append(target_sequence)

                current_index += 1

            inputs = self.token_ids_to_tensor(input_rows)
            targets = self.token_ids_to_tensor(output_rows)

            yield inputs, targets



if __name__ == "__main__":

    txt_dir = "../data/input.txt"
    text = open(txt_dir, encoding="utf-8").read() # change to read biger files

    tk = Tokenizer(text)

    dl = Data_Loader()
    print(dl.text_to_tensor("hello", tk))
