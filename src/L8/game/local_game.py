from abc import ABC

from L8.game.game import Game
from L8.messages.english import INITIALIZING_LOCAL_GAME, FINISH_LOCAL_GAME


class LocalGame(Game, ABC):

    def initialize(self):
        print(INITIALIZING_LOCAL_GAME)

    def tear_down_game(self):
        print(FINISH_LOCAL_GAME)
