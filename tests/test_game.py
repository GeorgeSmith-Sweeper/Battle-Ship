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
        ui = TerminalUi()
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
        hit = False

        board.state = MagicMock(return_value = board_state)
        board.add_to_board = MagicMock(return_value = board_state_after_ship_placed)
        board.update = MagicMock()
        board.format = MagicMock(return_value = formatted_board)
        validate.spot_occupied = MagicMock(return_value = user_shot_choice)
        validate.board_full = MagicMock(return_value = True)
        ui.get_input = MagicMock(return_value = user_shot_choice)
        ui.display = MagicMock()

        new_game = Game(board, ui, validate, ships, place)
        new_game.play()
        
        board.add_to_board.assert_called_with(ships.all_ships, place, ship_orientation)
        ui.display.assert_called()
        validate.board_full.assert_called_with(board.state)
        validate.spot_occupied.assert_called_with(board.state, ui, ships.all_ships)
        board.update.assert_called_with(user_shot_choice, hit)
