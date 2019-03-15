from abc import abstractmethod, ABC

from L8.board.board import Board


class Game(ABC):

    @abstractmethod
    def init(self):
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
