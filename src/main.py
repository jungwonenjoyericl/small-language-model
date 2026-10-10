
from tokenizer import Tokenizer
from data_loader import Data_Loader

tokenizer = Tokenizer()
data_pipeline = Data_Loader()

file_path = "../data/input.txt"
total_characters : int = 0 # to be able to split into train/val_data

# TODO:
# run this once, save into file and reuse vocab (incase new files for training contains new symbols, which can obstruct the current vocab)
for chunk in data_pipeline.read_chunks(file_path): 
    tokenizer.collect_characters(chunk)
    total_characters += len(chunk)

tokenizer.build_vocab()




train_path, val_path = data_pipeline.preprocess(file_path, total_characters, tokenizer) 

