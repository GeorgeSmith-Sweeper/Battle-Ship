from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.board import Board
from core.ui import TerminalUi
from core.validate import Validate
from play import Game

class TestPlayGame(TestCase):

    def test_play_runs_the_correct_methods(self):
        terminal_ui = TerminalUi()
        board = Board()
        validate = Validate()

        board_state = [[None]]
        user_shot_choice = 'A1'
        state_after_valid_spot_choice = [['X']]
        formatted_board = '[]'

        board.state = MagicMock(return_value = board_state)
        validate.spot_exists = MagicMock(return_value = user_shot_choice)
        validate.spot_occupied = MagicMock(return_value = user_shot_choice)
        validate.board_full = MagicMock(return_value = True)
        board.update = MagicMock(return_value = state_after_valid_spot_choice)
        board.format = MagicMock(return_value = formatted_board)

        terminal_ui.get_input = MagicMock(return_value = user_shot_choice)
        terminal_ui.display = MagicMock()

        new_game = Game(board, terminal_ui, validate)

        new_game.play()
        # collaboration tests
        validate.board_full.assert_called_with(board.state)
        validate.spot_occupied.assert_called_with(board.state, terminal_ui)
        board.update.assert_called_with(user_shot_choice)
