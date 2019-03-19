from abc import ABC, abstractmethod

from L8.board.board import Board


class Brain(ABC):

    @abstractmethod
    def calculate_next_move(self, board: Board) -> tuple:
        raise NotImplementedError
