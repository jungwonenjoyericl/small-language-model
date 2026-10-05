
class Tokenizer:
    def __init__(self, text : str) -> None: 
        self.unique_chars = sorted(set(text)) # not unique char list for now, just text
        self.stoi = {char: i for i, char in enumerate(self.unique_chars)} # string to token ID
        self.itos = {i: char for i, char in enumerate(self.unique_chars)} # Token ID to string

    def encode(self, text : str) -> list[int]:
        encoded_text = [self.stoi[char] for char in text]
        return encoded_text

    def decode(self, token_ids : list[int]) -> str:
        decoded_text = "".join([self.itos[id] for id in token_ids])
        return decoded_text

if __name__ == "__main__":

    text = open("../data/input.txt", encoding="utf-8").read()

    unique_chars = sorted(set(text)) # do sorting own logic

    tk = Tokenizer(text)
    print(tk.encode("hello"))
