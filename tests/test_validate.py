from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.validate import Validate
from core.board import Board
from core.ui import TerminalUi
from core.ships import Ships

class TestValidations(TestCase):
    def setUp(self):
        self.ships = Ships()
        self.validate = Validate()
        self.board = Board()
        self.board_with_ships = [
                ['AC', None, None, None, None, None, None, None, None, None],
                ['AC', None, None, None, None, None, None, None, None, None],
                ['AC', None, None, None, None, None, None, None, None, None],
                ['AC', None, None, None, 'C', None, None, None, None, None],
                ['AC', 'D', None, None, 'C', None, None, None, None, None],
                [None, 'D', None, None, 'C', None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, 'B', 'B', 'B', 'B'],
                [None, None, None, None, None, None, None, None, None, None],
                ['S', 'S', 'S', None, None, None, None, None, None, None],
                ]

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
       ui = TerminalUi()
       user_shot_choice = 'A1'
       self.assertEqual(self.validate.spot_exists(ui), 'A1')

    @patch('core.ui.TerminalUi.get_input', side_effect = ['A35', 'A1'])
    def test_spot_exists_prompts_the_user_if_spot_is_invalid(self, mocks):
       ui = TerminalUi()
       invalid_msg = 'Spot does not exist, Try again'
       ui.display = MagicMock()

       self.validate.spot_exists(ui)

       ui.display.assert_called_with(invalid_msg)

    @patch('core.validate.Validate.spot_exists', return_value= 'A2')
    def test_user_choice_is_returned_when_spot_is_not_occupied(self, mock1):
        ui = TerminalUi()
        user_shot_choice = 'A2'
        self.board.state = [
               ['X', None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               ]

        self.assertEqual(self.validate.spot_occupied(self.board.state, ui, self.ships.all_ships), 'A2')

    @patch('core.validate.Validate.spot_exists', side_effect = ['A1', 'A2'])
    @patch('core.ui.TerminalUi.get_input', side_effect = ['A2'])
    def test_spot_occupied_prompts_the_user_if_spot_is_occupied(self, mock1, mock2):
       validate = Validate()
       ui = TerminalUi()
       invalid_msg = 'That spot is occupied. Pick a different spot'
       ui.display = MagicMock()
       self.board.state = [
               ['X', None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               ]

       validate.spot_occupied(self.board.state, ui, self.ships.all_ships)

       ui.display.assert_called_with(invalid_msg)
    '''
    @patch('core.validate.Validate.spot_exists', side_effect = ['A1', 'A2'])
    @patch('core.ui.TerminalUi.get_input', side_effect = ['A2'])
    def test_spot_occupied_does_not_prompt_user_if_a_ship_is_hit(self, mock1, mock2):
       validate = Validate()
       ui = TerminalUi()
       ui.display = MagicMock()
       self.board.state = self.board_with_ships 

       validate.spot_occupied(self.board.state, ui, self.ships.all_ships)

       ui.display.assert_not_called()
    '''
    def test_board_full_returns_True_if_there_are_no_empty_spots_on_the_board(self):
        self.board.state = [
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ]
        self.assertEqual(self.validate.board_full(self.board.state), True)

    def test_board_full_returns_False_if_there_are_empty_spots_on_the_board(self):
        self.board.state = [
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
            ]
        self.assertEqual(self.validate.board_full(self.board.state), False)

    def test_hitting_a_ship_displays_msg_and_returns_true(self):
        ui = TerminalUi()
        ui.display = MagicMock()
        shot = 'A2'
        all_ships = self.ships.all_ships
        ship_hit_msg = 'You hit a ship!'    
        
        hit = self.validate.hit_ship(self.board_with_ships, shot, all_ships, ui)
        
        ui.display.assert_called_with(ship_hit_msg)
        self.assertEqual(hit, True)

    def test_missing_a_ship_displays_miss_msg_and_returns_False(self):
        ui = TerminalUi()
        ui.display = MagicMock()
        shot = 'A9'
        all_ships = self.ships.all_ships
        ship_hit_msg = 'Miss!'    
        
        hit = self.validate.hit_ship(self.board_with_ships, shot, all_ships, ui)
        
        ui.display.assert_called_with(ship_hit_msg)
        self.assertEqual(hit, False)
