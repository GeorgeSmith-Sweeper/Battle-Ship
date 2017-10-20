from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.ui import TerminalUi
from core.board import Board
from io import StringIO
from core.ships import Ships

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

    @patch('core.ui.TerminalUi.get_input', return_value='hello')
    def test_get_input_returns_a_users_input(self, mock):
        self.assertEqual(self.correct_response(), 'it works')

class TestFormat(TestCase):
    def setUp(self):
        self.board_with_ships = [
                ['AC', 'AC', 'AC', 'AC', 'AC', None, None, None, None, 'S'],
                [None, None, None, None, None, None, None, None, None, 'S'],
                [None, None, None, None, None, None, None, None, None, 'S'],
                [None, None, None, None, 'C', None, None, None, None, None],
                [None, 'D', None, None, 'C', None, None, None, None, None],
                [None, 'D', None, None, 'C', None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, 'B', 'B', 'B', 'B'],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]
        self.board_with_ships_and_moves = [
                ['Hit', 'AC', 'AC', 'AC', 'AC', None, None, None, None, 'S'],
                ['Miss', None, None, None, None, None, None, None, None, 'S'],
                [None, None, None, None, None, None, None, None, None, 'S'],
                [None, None, None, None, 'C', None, None, None, None, None],
                [None, 'D', None, None, 'C', None, None, None, None, None],
                [None, 'D', None, None, 'C', None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, 'B', 'B', 'B', 'B'],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]

        self.ships = Ships()
    
    def test_less_then_board_len_add_row_numbers_returns_correctly_formatted_row(self):
        board = Board()
        ui = TerminalUi()
        current_row = 0
        total_rows = 10
        row_number = ' 1 '

        formatted_row_number = ui.add_row_number(current_row, total_rows)
        self.assertEqual(formatted_row_number, row_number)
    
    def test_add_row_numbers_returns_correctly_formats_dbl_digit_rows(self):
        board = Board()
        ui = TerminalUi()
        current_row = 9
        total_rows = 10
        row_number = '10 '
        
        formatted_row_number = ui.add_row_number(current_row, total_rows)
        self.assertEqual(formatted_row_number, row_number)

    def test_board_is_formatted_correctly_with_ships_before_moves(self):
        board = Board()
        ui = TerminalUi() 
        board_with_hidden_ships = """
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
        formatted_board = ui.format(self.board_with_ships, self.ships.all_ships)
        self.assertEqual(formatted_board, board_with_hidden_ships)

    def test_board_is_formatted_correctly_with_an_shots_taken(self):
        board = Board()
        ui = TerminalUi()
        occupied_board = """
    A  B  C  D  E  F  G  H  I  J
 1 [H][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 2 [M][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 3 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 4 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 5 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 6 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 7 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 8 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 9 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
10 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
"""
        formatted_board = ui.format(self.board_with_ships_and_moves, self.ships.all_ships)

        self.assertEqual(formatted_board, occupied_board)
