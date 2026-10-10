
class Tokenizer:
    def __init__(self):
        self.unique_characters : list[str] = list()

    def collect_characters(self, text : str) -> None:
        unique_chars : set[str] = set(text) 

        for char in unique_chars: 
            if char not in self.unique_characters:
                self.unique_characters.append(char)
        self.unique_characters = sorted(self.unique_characters)

    def build_vocab(self) -> None: 
        self.stoi : dict[str , int] = {char: i for i, char in enumerate(self.unique_characters)} # string to token ID
        self.itos : dict[int , str] = {i: char for i, char in enumerate(self.unique_characters)} # Token ID to string

    def encode(self, text : str) -> list[int]:
        encoded_text : list[int] = [self.stoi[char] for char in text]
        return encoded_text

    def decode(self, token_ids : list[int]) -> str:
        decoded_text : str = "".join([self.itos[id] for id in token_ids])
        return decoded_text




if __name__ == "__main__":

    text = open("../data/input.txt", encoding="utf-8").read()

    unique_chars = sorted(set(text)) # do sorting own logic

    tk = Tokenizer(text)
    print(tk.encode("hello"))
