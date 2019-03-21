import random
import math

from L8.board.board import Board
from L8.board.tic_tac_toe_board import TicTacToeBoard
from L8.constants.constants import GameLevel
from L8.game.game_token import GameToken
from L8.game.tic_tac_toe_game import TicTacToeGame
from L8.player.ai.brain import Brain


class TicTacToeBrain(Brain):

    def __init__(self, level: GameLevel):
        super().__init__(level)

    def easy_mode(self, board: Board, game_token: GameToken) -> tuple:
        possible_moves = self.get_empty_spots(board)

        move = random.choice(possible_moves)
        return move

    def hard_mode(self, board: Board, game_token: GameToken) -> tuple:
        opponent_token = [t for t in TicTacToeGame.LEGAL_TOKENS if t is not game_token][0]
        move = self.minimax(board, game_token, opponent_token, is_ais_turn=True)[1]
        return move

    @staticmethod
    def get_empty_spots(board: Board) -> list:
        empty_spots = []

        for i, row in enumerate(board.current_state):
            for j, val in enumerate(row):
                if val is None:
                    empty_spots.append((i, j))

        return empty_spots

    @staticmethod
    def minimax(board: Board, game_token: GameToken, opponent_token: GameToken, is_ais_turn: bool):
        winner = TicTacToeBrain.calculate_winner(board)

        if winner:
            if is_ais_turn:
                return -1, None
            else:
                return 1, None

        move = None
        score = -math.inf

        for m in TicTacToeBrain.get_empty_spots(board):
            copy_board = [row.copy() for row in board.current_state]
            new_board = TicTacToeBoard()
            new_board.current_state = copy_board

            if is_ais_turn:
                new_board.current_state[m[0]][m[1]] = game_token
            else:
                new_board.current_state[m[0]][m[1]] = opponent_token

            score_for_new_move = -TicTacToeBrain.minimax(new_board, game_token, opponent_token, not is_ais_turn)[0]

            if score_for_new_move > score:
                score = score_for_new_move
                move = m

        if move is None:
            return 0, None

        return score, move

    @staticmethod
    def calculate_winner(board: Board):
        # Check if we have a winner
        for x, row in enumerate(board.current_state):
            for y, g_token in enumerate(row):

                # There will be no winner combination on this row/column
                if g_token is None:
                    continue

                if TicTacToeBrain.check_complete_line_in_board(board, g_token, x, y):
                    return g_token

        # Check if there are no more places to put a game_token
        for row in board.current_state:
            for g_token in row:
                if g_token is None:
                    return None

    @staticmethod
    def check_complete_line_in_board(board: Board, val: GameToken, x: int, y: int):
        """
        Checks if there are exactly three tokens equal to val horizontally, vertically and diagonally on the board
        respective to x and y
        :param val: a str representing the game_token to look for
        :param x: an int representing the original X coordinate of val
        :param y: an int representing the original Y coordinate of val
        :return: True if a line of successive val was found, False if otherwise
        """
        num_of_same_tokens = 0
        len_of_board = len(board.current_state)

        # Check horizontally
        for j in range(len_of_board):
            if board.current_state[x][j] == val:
                num_of_same_tokens += 1
            else:
                break

        if num_of_same_tokens == 3:
            return True

        num_of_same_tokens = 0

        # Check vertically
        for i in range(len_of_board):
            if board.current_state[i][y] == val:
                num_of_same_tokens += 1
            else:
                break

        if num_of_same_tokens == 3:
            return True

        num_of_same_tokens = 0

        # Check diagonally top to bottom, but only if we can do so
        if (x, y) in ((0, 0), (1, 1), (2, 2), (2, 0), (0, 2)):

            # Left to right:
            for i in range(len_of_board):
                if val != board.current_state[i][i]:
                    break
                else:
                    num_of_same_tokens += 1

            if num_of_same_tokens == 3:
                return True

            num_of_same_tokens = 0

            # Right to left
            for k in range(len_of_board):
                i = 0 + k
                j = 2 - k
                if val == board.current_state[i][j]:
                    num_of_same_tokens += 1

            return num_of_same_tokens == 3

        else:
            return False
