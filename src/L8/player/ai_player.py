from L8.board.board import Board
from L8.constants.constants import GAME_TOKEN, MOVE
from L8.game.gametoken import GameToken
from L8.player.ai.brain import Brain
from L8.player.player import Player
from L8.ui.ui import UI


class AIPlayer(Player):

    PLAYER_NUM = 1

    def __init__(self, brain: Brain, ui: UI, token: GameToken):
        super().__init__(token, ui)
        self.brain = brain

    def generate_name(self) -> str:
        self_name = f"AI_{AIPlayer.PLAYER_NUM}"
        AIPlayer.PLAYER_NUM += 1
        return self_name

    def make_move(self, board: Board) -> dict:
        move = self.brain.calculate_next_move(board)

        return {
            GAME_TOKEN: self.token,
            MOVE: move
        }
