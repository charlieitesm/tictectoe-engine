from abc import abstractmethod, ABC
from argparse import Namespace

from L8.board.board import Board


class Game(ABC):

    @abstractmethod
    def initialize(self):
        raise NotImplementedError

    @abstractmethod
    def play(self):
        raise NotImplementedError

    @abstractmethod
    def is_valid_move(self, move: dict) -> bool:
        raise NotImplementedError

    @abstractmethod
    def is_game_over(self, board: Board) -> bool:
        raise NotImplementedError

    @abstractmethod
    def finish_game(self):
        raise NotImplementedError


class GameFactory:

    @staticmethod
    def build_game(args: Namespace) -> Game:
        pass
