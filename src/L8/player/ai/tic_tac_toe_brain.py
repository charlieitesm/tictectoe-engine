from L8.board.board import Board
from L8.player.ai.brain import Brain


class TicTacToeBrain(Brain):

    def calculate_next_move(self, board: Board) -> tuple:
        raise NotImplementedError
