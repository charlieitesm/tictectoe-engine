from abc import abstractmethod, ABC

from L8.board.board import Board


class Player(ABC):

    def __init__(self):
        self.name = self.generate_name()

    @abstractmethod
    def make_move(self, board: Board) -> dict:
        raise NotImplementedError

    @abstractmethod
    def generate_name(self) -> str:
        raise NotImplementedError
