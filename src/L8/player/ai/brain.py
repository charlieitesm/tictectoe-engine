from abc import ABC, abstractmethod

from L8.board.board import Board
from L8.constants.constants import GameLevel
from L8.game.game_token import GameToken


class Brain(ABC):

    def __init__(self, level: GameLevel):
        self.level = level

        if level == GameLevel.EASY:
            self.calculate_next_move = self.easy_mode
        else:
            self.calculate_next_move = self.hard_mode

    @abstractmethod
    def easy_mode(self, board: Board, game_token: GameToken) -> tuple:
        raise NotImplementedError

    @abstractmethod
    def hard_mode(self, board: Board, game_token: GameToken) -> tuple:
        raise NotImplementedError
