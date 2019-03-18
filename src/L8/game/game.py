from abc import abstractmethod, ABC
from argparse import Namespace

from L8.board.board import Board
from L8.constants.constants import MOVE, TOKEN
from L8.messages.english import ILLEGAL_MOVE


class Game(ABC):

    def __init__(self):
        self.board = None
        self.players = None

    @abstractmethod
    def initialize_resources(self):
        raise NotImplementedError

    @abstractmethod
    def set_up_game(self):
        raise NotImplementedError

    def play(self):
        # This will contain the main game loop
        is_game_over_yet = False

        while not is_game_over_yet:

            # Ask each of the players for their move
            for player in self.players:

                player.ui.output(f"***** {player}'s turn! ******")
                player.ui.output(self.board)
                move = player.make_move(self.board)

                # Check that the move is legal in the context of the board
                while not self.is_valid_move(move):
                    player.ui.output(ILLEGAL_MOVE)
                    move = player.make_move(self.board)

                # Apply the player's move to the board since we now know it was legal
                move_x, move_y = move[MOVE]
                self.board[move_x][move_y] = move[TOKEN]

                is_game_over_yet = self.is_game_over(self.board)

                # If the game has ended, break the player loop which in turn will break the game loop
                if is_game_over_yet:
                    break

        # Leave every concrete game to decide what it need to do after a game is completed
        self.finish_game()
        self.release_resources()

    @abstractmethod
    def is_valid_move(self, move: dict) -> bool:
        raise NotImplementedError

    @abstractmethod
    def is_game_over(self, board: Board) -> bool:
        raise NotImplementedError

    @abstractmethod
    def finish_game(self):
        raise NotImplementedError

    @abstractmethod
    def release_resources(self):
        raise NotImplementedError


class GameFactory:

    @staticmethod
    def build_game(args: Namespace) -> Game:
        raise NotImplementedError
