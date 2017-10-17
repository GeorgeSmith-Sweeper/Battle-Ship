from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.board import Board
from core.placement import Place


class TestBoard(TestCase):
    
    def setUp(self):
       self.empty_board = [
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
       self.assertEqual(board.state, self.empty_board)

    @patch('core.placement.Place.create_random_num', return_value = 0)
    @patch('core.placement.Place.create_random_num', return_value = 0)
    def test_ship_added_to_row_if_there_is_room(self, mock1, mock2):
        board = Board()
        place = Place()
        state_after_move = [
                ['AC', 'AC', 'AC', 'AC', 'AC', None, None, None, None, None],
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
        all_ships = [{
            'symbol': 'AC',
            'size': 5,
            }]
        ship_orientation = 'row'
        board.add_to_board(all_ships, place, ship_orientation)
        self.assertEqual(board.state, state_after_move)

    @patch('core.placement.Place.create_random_num', return_value = 0)
    @patch('core.placement.Place.create_random_num', return_value = 0)
    
    def test_ship__added_to_column_if_there_is_room(self, mock1, mock2):
        board = Board()
        place = Place()
        state_after_move = [
                ['AC', None, None, None, None, None, None, None, None, None],
                ['AC', None, None, None, None, None, None, None, None, None],
                ['AC', None, None, None, None, None, None, None, None, None],
                ['AC', None, None, None, None, None, None, None, None, None],
                ['AC', None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]
        board.state = [
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
        all_ships = [{
            'symbol': 'AC',
            'size': 5,
            }]
        ship_orientation = 'column'
        board.add_to_board(all_ships, place, ship_orientation)
        self.assertEqual(board.state, state_after_move)
