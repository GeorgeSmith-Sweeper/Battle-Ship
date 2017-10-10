from unittest import TestCase, mock
from unittest.mock import patch, MagicMock, call
from play import Game, TerminalUi, Board, Validate
from io import StringIO
import sys

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
        board.update = MagicMock(return_value = state_after_valid_spot_choice)
        board.format = MagicMock(return_value = formatted_board)

        terminal_ui.get_input = MagicMock(return_value = user_shot_choice)
        terminal_ui.display = MagicMock()

        new_game = Game(board, terminal_ui, validate)

        new_game.play()
        # collaboration tests
        terminal_ui.display.assert_called()
        terminal_ui.get_input.assert_called()
        validate.spot_exists.assert_called_with(user_shot_choice, terminal_ui)
        validate.spot_occupied.assert_called_with(user_shot_choice, board.state, terminal_ui)
        board.update.assert_called_with(user_shot_choice)

class TestTerminalUi(TestCase):

    def test_terminal_displays_string_passed_to_it(self):
       ui = TerminalUi()
       with mock.patch('sys.stdout', new=StringIO()) as fake_stdout:
           ui.display('Welcome to Battleship')
       self.assertEqual(fake_stdout.getvalue(), 'Welcome to Battleship\n')

    def correct_response(self):
        ui = TerminalUi()
        answer = ui.get_input("Enter hello: ")
        if answer == 'hello':
            return 'it works'

    @patch('play.TerminalUi.get_input', return_value='hello')
    def test_get_input_returns_a_users_input(self, input):
        self.assertEqual(self.correct_response(), 'it works')

class TestBoard(TestCase):
    def test_board_is_formatted_correctly_with_empty_board(self):
        board = Board()
        initial_board = """
    A  B  C  D  E  F  G  H  I  J
 1 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 2 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 3 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 4 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 5 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 6 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 7 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 8 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 9 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
10 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
"""
        formatted_board = board.format()

        self.assertEqual(formatted_board, initial_board)

    def test_board_is_formatted_correctly_with_an_occupied_board(self):
        board = Board()
        board.update('A1')
        occupied_board = """
    A  B  C  D  E  F  G  H  I  J
 1 [X][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 2 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 3 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 4 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 5 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 6 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 7 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 8 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 9 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
10 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
"""
        formatted_board = board.format()

        self.assertEqual(formatted_board, occupied_board)

    def test_board_is_initialized_with_an_empty_state(self):
       board = Board()
       initial_board_state = [
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
       self.assertEqual(board.state, initial_board_state)

class TestValidations(TestCase):
    def test_Validate_is_initialized_with_a_letters_list(self):
        validate = Validate()
        letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        self.assertEqual(validate.letters, letters_list)

    def test_Validate_is_initialized_with_a_numbers_list(self):
        validate = Validate()
        numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        self.assertEqual(validate.numbers, numbers_list)

    def test_Validate_is_initialized_with_a_all_spots_list(self):
        validate = Validate()
        all_spots_list = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10']

        self.assertEqual(validate.all_spots, all_spots_list)

    def test_spot_exists_returns_user_input_when_choosen_spot_exists(self):
       validate = Validate()
       ui = TerminalUi()
       user_shot_choice = 'A1'
       self.assertEqual(validate.spot_exists(user_shot_choice, ui), 'A1')
    '''
    @patch('play.TerminalUi.get_input', return_value= 'A1')
    def test_spot_exists_prompts_the_user_if_spot_is_invalid(self, input):
       validate = Validate()
       ui = TerminalUi()
       invalid_msg = 'Spot does not exist, Try again'
       user_shot_choice = 'A35'
       ui.display = MagicMock()

       validate.spot_exists(user_shot_choice, ui)

       ui.display.assert_called_with(invalid_msg)
       assert input() == 'A1'
    '''
    def test_user_choice_is_returned_when_spot_is_not_occupied(self):
        validate = Validate()
        board = Board()
        ui = TerminalUi()
        user_shot_choice = 'A2'
        board.state = [
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

        self.assertEqual(validate.spot_occupied(user_shot_choice, board.state, ui), 'A2')

