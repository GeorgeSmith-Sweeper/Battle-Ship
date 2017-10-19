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
        self.ships = Ships()

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

    def test_board_is_formatted_correctly_with_an_occupied_board(self):
        board = Board()
        ui = TerminalUi()
        hit = True
        board.update('A2', hit)
        occupied_board = """
    A  B  C  D  E  F  G  H  I  J
 1 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 2 [X][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 3 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 4 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 5 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 6 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 7 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 8 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 9 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
10 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
"""
        formatted_board = ui.format(board.state, self.ships.all_ships)

        self.assertEqual(formatted_board, occupied_board)
