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
        ships = Ships()
        ui = TerminalUi()
        human_board = Board(ships)
        comp_board = Board(ships)
        validate = Validate()
        place = Place()

        board_state = [[None]]
        board_state_after_ship_placed = [['AC', 'AC', 'AC', 'AC', 'AC']]
        user_shot_choice = 'A1'
        state_after_valid_spot_choice = [['H', 'AC', 'AC', 'AC', 'AC']]
        formatted_board = '[]'
        ship_orientation = 'row'
        ship_size = 5
        hit = False

        comp_board.state = MagicMock(return_value = board_state)
        comp_board.add_to_board = MagicMock(return_value = board_state_after_ship_placed)
        comp_board.update = MagicMock()
        validate.spot_occupied = MagicMock(return_value = user_shot_choice)
        validate.board_full = MagicMock(return_value = True)
        validate.hit_ship = MagicMock(return_value = False)
        
        ui.get_input = MagicMock(return_value = user_shot_choice)
        ui.display = MagicMock()

        new_game = Game(comp_board, human_board, ui, validate, place)
        new_game.play()

        comp_board.add_to_board.assert_called_with(place, ship_orientation)
        ui.display.assert_called()
        validate.board_full.assert_called_with(comp_board.state)
        validate.spot_occupied.assert_called_with(comp_board.state, ui, comp_board.ships.all_ships)
        validate.hit_ship(comp_board.state, user_shot_choice, comp_board.ships.all_ships) 
        comp_board.update.assert_called_with(user_shot_choice, hit)
