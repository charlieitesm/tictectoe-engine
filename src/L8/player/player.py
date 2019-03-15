from abc import abstractmethod, ABC

from L8.board.board import Board


class Player(ABC):

    @abstractmethod
    def make_move(self, board: Board) -> dict:
        raise NotImplementedError
