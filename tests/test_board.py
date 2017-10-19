from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.board import Board
from core.placement import Place
from core.validate import Validate

class TestBoard(TestCase):

    def setUp(self):
       self.board = Board()
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
       self.board_with_a_hit = [
                ['AC', 'Hit', 'AC', 'AC', 'AC', None, None, None, None, 'S'],
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

    def test_Hit_is_added_to_board_if_the_user_hit_a_ship(self):
        user_shot_choice = 'A2'
        self.board.state = [
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
        hit = True
        
        self.board.update(user_shot_choice, hit)
        self.assertEqual(self.board.state, self.board_with_a_hit)
    
    @patch('core.placement.Place.create_random_num', return_value = 0)
    @patch('core.placement.Place.create_random_num', return_value = 0)
    def test_ship_added_to_row_if_there_is_room(self, mock1, mock2):
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
        self.board.add_to_board(all_ships, place, ship_orientation)
        self.assertEqual(self.board.state, state_after_move)

    @patch('core.placement.Place.create_random_num', return_value = 0)
    @patch('core.placement.Place.create_random_num', return_value = 0)
    def test_ship__added_to_column_if_there_is_room(self, mock1, mock2):
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
        all_ships = [{
            'symbol': 'AC',
            'size': 5,
            }]
        ship_orientation = 'column'
        self.board.add_to_board(all_ships, place, ship_orientation)
        self.assertEqual(self.board.state, state_after_move)
