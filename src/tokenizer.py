
class Tokenizer:
    def __int__(self):
        self.unique_characters : set[str]= {}

    def collect_characters(self, text : str) -> None:
        unique_chars : set[str] = set(text)
        self.unique_characters.update(unique_chars)

    def build_vocab(self, text : str) -> None: 
        self.unique_chars : {str} = sorted(set(text)) # not unique char list for now, just text
        self.stoi : dict[str : int] = {char: i for i, char in enumerate(self.unique_chars)} # string to token ID
        self.itos : dict[int : str] = {i: char for i, char in enumerate(self.unique_chars)} # Token ID to string

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
