from abc import ABC, abstractmethod

from L8.board.board import Board
from L8.constants.constants import GameLevel


class Brain(ABC):

    def __init__(self, level: GameLevel):
        self.level = level

        if level == GameLevel.EASY:
            self.calculate_next_move = self.easy_mode
        else:
            self.calculate_next_move = self.hard_mode

    @abstractmethod
    def easy_mode(self, board: Board) -> tuple:
        raise NotImplementedError

    @abstractmethod
    def hard_mode(self, board: Board) -> tuple:
        raise NotImplementedError
