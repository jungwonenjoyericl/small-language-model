
from tokenizer import Tokenizer
from data_loader import Data_Loader

tokenizer = Tokenizer
data_pipeline = Data_Loader

file_path = "../data/input.txt"

total_characters : int = 0 # to be able to split into train/val_data
for chunk in data_pipeline.read_chunks(file_path, 10_000):
    tokenizer.collect_characters(chunk)
    total_characters += len(chunk)

tokenizer.build_vocab()

data_pipeline.iter_training_batches(file_path, 10_000, total_characters) # default val for split_ratio (9 train:1 val)

