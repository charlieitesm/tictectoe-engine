from abc import abstractmethod, ABC

from L8.board.board import Board


class Player(ABC):

    def __init__(self):
        self.name = ""

    @abstractmethod
    def make_move(self, board: Board) -> dict:
        raise NotImplementedError
