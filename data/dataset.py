from datasets import load_dataset

# change to download other huggingface training data
dataset = load_dataset(
    "roneneldan/TinyStories",
    split="train",
    streaming=True,
)


with open("data/raw/TinyStories.txt", "w", encoding="utf-8") as f:
    for row in dataset:
        f.write(row["text"])
        f.write("\n\n")
