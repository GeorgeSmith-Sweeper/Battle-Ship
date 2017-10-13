from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.board import Board
from core.ui import TerminalUi
from core.validate import Validate
from core.ships import Ships
from core.placement import Place
from play import Game


class TestPlayGame(TestCase):

    def test_play_runs_the_correct_methods(self):
        terminal_ui = TerminalUi()
        board = Board()
        validate = Validate()
        ships = Ships()
        place = Place()

        board_state = [[None]]
        board_state_after_ship_placed = [['AC', 'AC', 'AC', 'AC', 'AC']]
        user_shot_choice = 'A1'
        state_after_valid_spot_choice = [['H', 'AC', 'AC', 'AC', 'AC']]
        formatted_board = '[]'
        ship_orientation = 'row'
        ship_size = 5


        board.state = MagicMock(return_value = board_state)
        place.ship_fit = MagicMock(return_value = board_state_after_ship_placed)
        validate.spot_occupied = MagicMock(return_value = user_shot_choice)
        validate.board_full = MagicMock(return_value = True)
        board.update = MagicMock(return_value = state_after_valid_spot_choice)
        board.format = MagicMock(return_value = formatted_board)
        terminal_ui.get_input = MagicMock(return_value = user_shot_choice)
        terminal_ui.display = MagicMock()

        new_game = Game(board, terminal_ui, validate, ships, place)

        new_game.play()


        place.ship_fit.assert_called()
        terminal_ui.display.assert_called()
        validate.board_full.assert_called_with(board.state)
        validate.spot_occupied.assert_called_with(board.state, terminal_ui)
        board.update.assert_called_with(user_shot_choice)
