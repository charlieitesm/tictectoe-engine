import random

from L8.board.board import Board
from L8.constants.constants import GameLevel
from L8.player.ai.brain import Brain


class TicTacToeBrain(Brain):

    def __init__(self, level: GameLevel):
        super().__init__(level)

    @staticmethod
    def easy_mode(board: Board) -> tuple:
        possible_moves = []

        for i, row in enumerate(board.current_state):
            for j, val in enumerate(row):
                if val is None:
                    possible_moves.append((i, j))

        move = random.choice(possible_moves)
        return move

    def hard_mode(self, board: Board):
        raise NotImplementedError
