from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.ui import TerminalUi
from core.board import Board
from io import StringIO
from helpers.board_helper import BoardHelper

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
    
    def test_ui_is_initialized_with_a_winning_msg_for_the_computer(self):
        ui = TerminalUi()
        COMP_WIN_MSG = 'The Computer has sunk all the ships! Game Over!'

        self.assertEqual(ui.COMP_WIN_MSG, COMP_WIN_MSG)

    def test_ui_is_initialized_with_a_winning_msg_for_humans(self):
        ui = TerminalUi()
        HUMAN_WIN_MSG = 'Congratulations, you\'ve has sunk all the computers ships! Game Over!'

        self.assertEqual(ui.HUMAN_WIN_MSG, HUMAN_WIN_MSG)

class TestFormat(TestCase):
    def setUp(self):
        self.ui = TerminalUi()
        self.board = Board()
        self.board_helper = BoardHelper(self.board.all_ships)
        self.missed_marker = '[' + '\033[35m' + 'M' + '\033[0m' + ']'
        self.hit_marker =  '[' + '\033[36m' + 'H' + '\033[0m' + ']'
        self.sunk_marker = '\033[41m' + '[S]' + '\033[0m'

    def test_ui_contains_the_ANSI_red_background_as_REDBG(self):
        redbg = '\033[41m'
        self.assertEqual(self.ui.REDBGCOLOR, redbg)
    
    def test_ui_contains_the_ANSI_magenta_text_as_MAGENTA(self):
        magenta = '\033[35m'
        self.assertEqual(self.ui.MAGENTA, magenta)
    
    def test_ui_contains_the_ANSI_cyan_text_as_CYAN(self):
        cyan = '\033[36m'
        self.assertEqual(self.ui.CYAN, cyan)

    def test_ui_contains_the_ANSI_attr_off_as_ENDCOLORS(self):
        attr_off = '\033[0m'
        self.assertEqual(self.ui.ENDCOLOR, attr_off)

    def test_less_then_board_len_add_row_numbers_returns_correctly_formatted_row(self):
        current_row = 0
        total_rows = 10
        row_number = ' 1 '

        formatted_row_number = self.ui.add_row_number(current_row, total_rows)
        self.assertEqual(formatted_row_number, row_number)
    
    def test_add_row_numbers_returns_correctly_formats_dbl_digit_rows(self):
        current_row = 9
        total_rows = 10
        row_number = '10 '
        
        formatted_row_number = self.ui.add_row_number(current_row, total_rows)
        self.assertEqual(formatted_row_number, row_number)
    
    def test_add_shot_marker_returns_brakets_when_a_spot_is_empty(self):
        empty_marker = '[ ]'
        row = 2
        column = 0
        formated_marker = self.ui.add_shot_marker(self.board_with_ships_and_moves, row, column, self.board.all_ships)

        self.assertEqual(formated_marker, empty_marker)

    def test_add_shot_marker_returns_M_when_a_ship_is_missed(self):
        missed_marker = self.missed_marker 
        row = 1
        column = 0
        board_with_hit_and_miss = self.board_helper.generate_board_with_hit_and_miss()
        formated_marker = self.ui.add_shot_marker(board_with_hit_and_miss, row, column, self.board.all_ships)

        self.assertEqual(formated_marker, missed_marker)

    def test_add_shot_marker_returns_H_when_a_ship_is_hit(self):
        hit_marker = self.hit_marker 
        row = 0
        column = 0
        board_with_hit_and_miss = self.board_helper.generate_board_with_hit_and_miss()
        formated_marker = self.ui.add_shot_marker(board_with_hit_and_miss, row, column, self.board.all_ships)

        self.assertEqual(formated_marker, hit_marker)
        
    def test_add_shot_marker_returns_brakets_when_a_spot_is_empty(self):
        sunk_marker = self.sunk_marker 
        row = 0
        column = 0
        board_with_a_sunken_ship = self.board_helper.generate_board_with_a_sunken_ship()
        formated_marker = self.ui.add_shot_marker(board_with_a_sunken_ship, row, column, self.board.all_ships)

        self.assertEqual(formated_marker, sunk_marker)
     
    def test_board_is_formatted_correctly_with_ships_before_moves(self):
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
        board_with_ships = self.board_helper.generate_board_with_ships()
        formatted_board = self.ui.format(board_with_ships, self.board.all_ships)
        self.assertEqual(formatted_board, board_with_hidden_ships)

    def test_board_is_formatted_correctly_with_an_shots_taken(self):
        M = self.missed_marker 
        H = self.hit_marker
        occupied_board = """
    A  B  C  D  E  F  G  H  I  J
 1 %s[ ][ ][ ][ ][ ][ ][ ][ ][ ]
 2 %s[ ][ ][ ][ ][ ][ ][ ][ ][ ]
 3 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 4 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 5 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 6 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 7 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 8 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 9 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
10 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
""" % (H, M)
        board_with_hit_and_miss = self.board_helper.generate_board_with_hit_and_miss()
        formatted_board = self.ui.format(board_with_hit_and_miss, self.board.all_ships)

        self.assertEqual(formatted_board, occupied_board)

    def test_board_is_formatted_correctly_with_a_sunken_ship(self):
        S = self.sunk_marker
        occupied_board = """
    A  B  C  D  E  F  G  H  I  J
 1 %s%s%s%s%s[ ][ ][ ][ ][ ]
 2 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 3 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 4 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 5 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 6 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 7 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 8 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 9 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
10 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
""" % (S, S, S, S, S)
        board_with_hit_and_miss = self.board_helper.generate_board_with_a_sunken_ship()
        formatted_board = self.ui.format(board_with_hit_and_miss, self.board.all_ships)

        self.assertEqual(formatted_board, occupied_board)

    def test_board_is_formatted_correctly_with_an_shots_taken(self):
        M = self.missed_marker 
        H = self.hit_marker
        occupied_board = """
    A  B  C  D  E  F  G  H  I  J
 1 %s[ ][ ][ ][ ][ ][ ][ ][ ][ ]
 2 %s[ ][ ][ ][ ][ ][ ][ ][ ][ ]
 3 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 4 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 5 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 6 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 7 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 8 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
 9 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
10 [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
""" % (H, M)
        board_with_hit_and_miss = self.board_helper.generate_board_with_hit_and_miss()
        formatted_board = self.ui.format(board_with_hit_and_miss, self.board.all_ships)

        self.assertEqual(formatted_board, occupied_board)
