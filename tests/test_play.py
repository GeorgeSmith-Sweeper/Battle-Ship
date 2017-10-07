from unittest import TestCase, mock
from unittest.mock import patch, MagicMock, call
from play import Game, TerminalUi, Board, SpotChooser
from core import board
from io import StringIO

class TestPlayGame(TestCase):

    def test_display_calls(self):
        terminal_ui = TerminalUi()
        board = Board()
        spot_chooser = SpotChooser(board)

        board_state = []
        user_input = 'A1'
        state_after_spot_choice = ['A1']
        formatted_board = '[]'

        board.update = MagicMock(return_value = board_state)
        spot_chooser.choose_a_spot = MagicMock(return_value = state_after_spot_choice)
        board.format = MagicMock(return_value = formatted_board)
        terminal_ui.get_input = MagicMock(return_value = user_input)
        terminal_ui.display = MagicMock()
        expected_calls = [call("Welcome to Battleship"), call(board.format()), call("Take your best shot")]
        
        new_game = Game(board, spot_chooser, terminal_ui) 

        new_game.play()
        
        self.assertEqual(terminal_ui.display.call_args_list, expected_calls)

        
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

####################################################################
class TestBoard(TestCase):
    def test_board_is_formatted_correctly_with_empty_board(self):
        board = Board()
        initial_board = """
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
[][][][][][][][][][]
"""
        formatted_board = board.format()

        self.assertEqual(formatted_board, initial_board) 

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
