from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.validate import Validate
from core.board import Board
from core.ui import TerminalUi
from core.ships import Ships
from helpers.board_helper import BoardHelper

class TestValidations(TestCase):

    def setUp(self):
        self.ships = Ships()
        self.board = Board(self.ships)
        self.board_helper = BoardHelper(self.ships)
        self.validate = Validate()
        self.ui = TerminalUi()

    def test_split_user_row_and_returns_a_single_letter_and_a_number_as_strings(self):
        user_shot_choice = 'A2'
        split_choice = ('A', '2')
        answer = self.validate.split_user_shot(user_shot_choice)
        self.assertEqual(answer, split_choice)

    def test_Validate_is_initialized_with_a_letters_list(self):
        col_lets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        self.assertEqual(self.validate.col_lets, col_lets)

    def test_Validate_is_initialized_with_a_numbers_list(self):
        row_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        self.assertEqual(self.validate.row_nums, row_nums)

    def test_Validate_is_initialized_with_a_all_spots_list(self):
        all_spots_list = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10']

        self.assertEqual(self.validate.all_spots, all_spots_list)

    @patch('core.ui.TerminalUi.get_input', return_value = 'A1')
    def test_spot_exists_returns_user_input_when_choosen_spot_exists(self, mock):
       user_shot_choice = 'A1'
       self.assertEqual(self.validate.spot_exists(self.ui), 'A1')
    
    def test_get_current_spot_returns_the_value_of_the_selected_spot_on_the_board(self):
       user_shot_choice = 'A1'
       board_with_ships = self.board_helper.generate_board_with_ships() 
       spot_value = self.validate.get_current_spot(board_with_ships, user_shot_choice) 
       aircraft_carrier = self.ships.all_ships[0]
       self.assertEqual(spot_value, aircraft_carrier)

    @patch('core.ui.TerminalUi.get_input', side_effect = ['A35', 'A1'])
    def test_spot_exists_prompts_the_user_if_spot_is_invalid(self, mocks):
       invalid_msg = 'Spot does not exist, Try again'
       self.ui.display = MagicMock()

       self.validate.spot_exists(self.ui)

       self.ui.display.assert_called_with(invalid_msg)

    @patch('core.validate.Validate.spot_exists', return_value= 'A2')
    def test_user_choice_is_returned_when_spot_is_not_occupied(self, mock1):
        user_shot_choice = 'A2'
        self.board.state = self.board_helper.generate_all_but_one()

        self.assertEqual(self.validate.spot_occupied(self.board.state, self.ui, self.ships.all_ships), 'A2')

    @patch('core.validate.Validate.spot_exists', side_effect = ['A1', 'A2'])
    @patch('core.ui.TerminalUi.get_input', side_effect = ['A2'])
    def test_spot_occupied_prompts_the_user_if_spot_is_occupied(self, mock1, mock2):
       invalid_msg = 'That spot is occupied. Pick a different spot'
       self.ui.display = MagicMock()
       self.board.state = self.board_helper.generate_all_but_one()
       self.validate.spot_occupied(self.board.state, self.ui, self.ships.all_ships)

       self.ui.display.assert_called_with(invalid_msg)
    
    def test_all_ships_sunk_returns_True_if_there_are_no_ships_left(self):
        self.board.state = self.board_helper.generate_full_board() 
        
        self.assertEqual(self.validate.all_ships_sunk(self.board.state, self.board.ships.all_ships), True)

    def test_all_ships_sunk_returns_False_if_there_are_ships_left(self):
        self.board.state = self.board_helper.generate_board_with_ships() 
        
        self.assertEqual(self.validate.all_ships_sunk(self.board.state, self.board.ships.all_ships), False)

    def test_hitting_a_ship_displays_msg_and_returns_str_Hit(self):
        self.ui.display = MagicMock()
        shot = 'A1'
        all_ships = self.ships.all_ships
        ship_hit_msg = 'You hit the Aircraft Carrier!'
        board_with_ships = self.board_helper.generate_board_with_ships() 
        is_hit = self.validate.hit_ship(board_with_ships, shot, all_ships, self.ui)

        self.ui.display.assert_called_with(ship_hit_msg)
        self.assertEqual(is_hit, 'Hit')

    def test_missing_a_ship_displays_miss_msg_and_returns_str_Miss(self):
        self.ui.display = MagicMock()
        shot = 'A9'
        all_ships = self.ships.all_ships
        board_with_ships = self.board_helper.generate_board_with_ships() 
        ship_hit_msg = 'Miss!'
        is_hit = self.validate.hit_ship(board_with_ships, shot, all_ships, self.ui)

        self.ui.display.assert_called_with(ship_hit_msg)
        self.assertEqual(is_hit, 'Miss')
    
    def test_ship_is_sunk_when_len_hit_locations_equals_ship_size(self):
        sunken_ship = {
                'name': 'Aircraft Carrier',
                'size': 5,
                'sunk': True,
                'hit_locations': [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],
                }
        
        self.ui.display = MagicMock()
        ship_sunk_msg = 'You sunk the Aircraft Carrier!'
        is_sunk = self.validate.is_ship_sunk(sunken_ship, self.ui)

        self.ui.display.assert_called_with(ship_sunk_msg)
        self.assertEqual(is_sunk, True)

    def test_ship_is_not_sunk_when_len_hit_locations_doesnt_equal_ship_size(self):
        ship_with_no_hits = {
                'name': 'Aircraft Carrier',
                'size': 5,
                'sunk': False,
                'hit_locations': [],
                }
    
        self.assertFalse(self.validate.is_ship_sunk(ship_with_no_hits, self.ui))

    def test_when_a_ship_is_hit_it_stores_the_location_of_the_hit(self):
        current_ship = {
                'name': 'Aircraft Carrier',
                'size': 5,
                'sunk': False,
                'hit_locations': [],
                } 
        
        ship_after_hit = {
                'name': 'Aircraft Carrier',
                'size': 5,
                'sunk': False,
                'hit_locations': [[0, 0]],
                }
        shot = 'A1' 
        self.assertEqual(self.validate.store_hits(current_ship, shot), ship_after_hit)
         
