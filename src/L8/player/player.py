from abc import abstractmethod, ABC

from L8.board.board import Board
from L8.token.token import Token


class Player(ABC):

    def __init__(self, token: Token):
        self.name = self.generate_name()
        self.token = token

    @abstractmethod
    def make_move(self, board: Board) -> dict:
        raise NotImplementedError

    @abstractmethod
    def generate_name(self) -> str:
        raise NotImplementedError

    def __str__(self):
        return self.name
