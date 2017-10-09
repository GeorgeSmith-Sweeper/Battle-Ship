from unittest import TestCase, mock
from unittest.mock import patch, MagicMock, call
from play import Game, TerminalUi, Board 
from io import StringIO

class TestPlayGame(TestCase):
    
    def test_play_runs_the_correct_methods(self):
        terminal_ui = TerminalUi()
        board = Board()

        board_state = [[None]]
        user_shot_choice = 'A1'
        state_after_valid_spot_choice = [['X']]
        formatted_board = '[]'
        
        board.state = MagicMock()
        board.spot_exists = MagicMock(return_value = True)
        board.spot_occupied = MagicMock(return_value = False)
        board.update = MagicMock(return_value = state_after_valid_spot_choice)
        board.format = MagicMock(return_value = formatted_board)
        
        terminal_ui.get_input = MagicMock(return_value = user_shot_choice)
        terminal_ui.display = MagicMock() 
        
        new_game = Game(board, terminal_ui) 

        new_game.play()
        # collaboration tests
        terminal_ui.display.assert_called()
        terminal_ui.get_input.assert_called()         
        board.spot_exists.assert_called_with(user_shot_choice)
        board.spot_occupied.assert_called_with(user_shot_choice)
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

    def test_spot_exists_returns_True_when__choosen_spot_exists(self):
       board = Board()
       user_shot_choice = 'A1' 
       self.assertEqual(board.spot_exists(user_shot_choice), True)
    
    def test_False_is_returned_when_shot_is_invalid(self):
       board = Board()
       user_shot_choice = 'A35' 
       self.assertEqual(board.spot_exists(user_shot_choice), False)
   
    def test_True_is_returned_when_spot_is_occupied(self):
        board = Board()
        user_shot_choice = 'A1'
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

        self.assertEqual(board.spot_occupied(user_shot_choice), True)

    def test_False_is_returned_when_spot_is_not_occupied(self):
        board = Board()
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

        self.assertEqual(board.spot_occupied(user_shot_choice), False)
        
    def test_board_state_is_updated_with_new_spot_choice(self):
        board = Board()
         
        state_after_spot_choice = [
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

        spot_choice = 'A1'
        board.update(spot_choice)
        self.assertEqual(board.state, state_after_spot_choice)
