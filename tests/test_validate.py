from unittest import TestCase
from unittest.mock import MagicMock
from core.validate import Validate
from core.board import Board
from core.ui import TerminalUi
from helpers.board_helper import BoardHelper
import helpers.constants as consts


class TestValidations(TestCase):

    def setUp(self):
        self.board = Board()
        self.board_helper = BoardHelper(self.board.all_ships)
        self.validate = Validate()
        self.ui = TerminalUi()

    def test_split_user_row_and_returns_a_single_letter_and_a_number_as_strings(self):
        user_shot_choice = 'A2'
        split_choice = ('A', '2')
        answer = self.validate.split_user_shot(user_shot_choice)
        self.assertEqual(answer, split_choice)

    def test_Validate_is_initialized_with_a_letters_list(self):
        col_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        self.assertEqual(self.validate.col_letters, col_letters)

    def test_Validate_is_initialized_with_a_numbers_list(self):
        row_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        self.assertEqual(self.validate.row_nums, row_nums)

    def test_Validate_is_initialized_with_a_all_spots_list(self):
        all_spots_list = self.board_helper.generate_all_spots()

        self.assertEqual(self.validate.all_spots, all_spots_list)

    def test_spot_exists_returns_True_if_spot_exists(self):
        user_shot_choice = 'A1'
        self.assertTrue(self.validate._spot_exists(user_shot_choice))

    def test_spot_exists_returns_False_if_the_spot_is_invalid(self):
        user_shot_choice = 'J4000'
        self.assertFalse(self.validate._spot_exists(user_shot_choice))

    def test_get_current_spot_returns_the_value_of_the_selected_spot_on_the_board(self):
        user_shot_choice = 'A1'
        board_with_ships = self.board_helper.generate_board_with_ships()
        spot_value = self.validate.get_current_spot(board_with_ships, user_shot_choice)
        aircraft_carrier = self.board.all_ships[0]
        self.assertEqual(spot_value, aircraft_carrier)

    def test_spot_occupied_returns_False_if_spot_is_not_occupied(self):
        user_shot_choice = 'A2'
        all_but_one = self.board_helper.generate_all_but_one()
        board = MagicMock(state=all_but_one, all_ships=self.board.all_ships)

        self.assertEqual(False, self.validate._spot_occupied(board, user_shot_choice))

    def test_spot_occupied_returns_true_if_spot_is_occupied(self):
        user_shot_choice = 'A1'
        all_but_one = self.board_helper.generate_all_but_one()
        board = MagicMock(state=all_but_one, all_ships=self.board.all_ships)
        self.validate._spot_occupied(board, user_shot_choice)

    def test_all_ships_sunk_returns_True_if_there_are_no_ships_left(self):
        full_board = self.board_helper.generate_full_board()
        all_sunken_ships = self.board_helper.generate_sunken_ships()
        board = MagicMock(state=full_board, all_ships=all_sunken_ships)
        self.assertEqual(self.validate.all_ships_sunk(board), True)

    def test_all_ships_sunk_returns_False_if_there_are_ships_left(self):
        board_with_ships = self.board_helper.generate_board_with_ships()
        board = MagicMock(state=board_with_ships, all_ships=self.board.all_ships)
        self.assertEqual(self.validate.all_ships_sunk(board), False)

    def test_hitting_a_ship_displays_msg_and_returns_str_Hit(self):
        shot = 'A1'
        board_with_ships = self.board_helper.generate_board_with_ships()
        board = MagicMock(state=board_with_ships, all_ships=self.board.all_ships)
        shot_result = self.validate.shot_result(board, shot)
        result = (consts.HIT, {'name': 'Aircraft Carrier', 'size': 5, 'hit_locations': [[0, 0]]})
        self.assertEqual(shot_result, result)

    def test_missing_a_ship_returns_str_Miss_and_None(self):
        shot = 'A9'
        board_with_ships = self.board_helper.generate_board_with_ships()
        board = MagicMock(state=board_with_ships, all_ships=self.board.all_ships)
        shot_result = self.validate.shot_result(board, shot)
        result = (consts.MISS, None)
        self.assertEqual(shot_result, result)

    def test_ship_is_sunk_when_len_hit_locations_equals_ship_size(self):
        sunken_ship = {
            'name': 'Aircraft Carrier',
            'size': 5,
            'hit_locations': [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],
        }
        is_sunk = self.validate._is_ship_sunk(sunken_ship)

        self.assertEqual(is_sunk, True)

    def test_ship_is_not_sunk_when_len_hit_locations_doesnt_equal_ship_size(self):
        ship_with_no_hits = {
            'name': 'Aircraft Carrier',
            'size': 5,
            'hit_locations': [],
        }

        self.assertFalse(self.validate._is_ship_sunk(ship_with_no_hits))

    def test_when_a_ship_is_hit_it_stores_the_location_of_the_hit(self):
        current_ship = {
            'name': 'Aircraft Carrier',
            'size': 5,
            'hit_locations': [],
        }
        ship_after_hit = {
            'name': 'Aircraft Carrier',
            'size': 5,
            'hit_locations': [[0, 0]]
        }
        shot = 'A1'

        self.assertEqual(self.validate._store_hits(current_ship, shot), ship_after_hit)
