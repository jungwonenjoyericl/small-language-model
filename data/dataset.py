from datasets import load_dataset

dataset = load_dataset(
    "roneneldan/TinyStories",
    split="train",
    streaming=True,
)


with open("input.txt", "w", encoding="utf-8") as f:
    for row in dataset:
        f.write(row["text"])
        f.write("\n\n")
