from abc import ABC


class Token(ABC):

    def __init__(self, token_symbol: str):
        self.token_symbol = token_symbol

    def __str__(self):
        return self.token_symbol

