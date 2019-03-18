from abc import ABC


class GameToken(ABC):

    def __init__(self, token_symbol: str):
        self.token_symbol = token_symbol

    def __str__(self):
        return self.token_symbol

