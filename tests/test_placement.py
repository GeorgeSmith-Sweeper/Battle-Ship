from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.board import Board
from core.ships import Ships
from core.placement import Place
from helpers.board_helper import BoardHelper

class TestPlace(TestCase):
    def setUp(self):
        self.ships = Ships()
        self.board = Board()
        self.place = Place()
        self.board_helper = BoardHelper(self.ships)

    def test_create_random_generates_a_num_from_0_to_9(self):
        zero_to_nine_list = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]
        random_num = self.place.create_random_num()
        self.assertIn(random_num, zero_to_nine_list)

    @patch('core.placement.Place.create_random_num', side_effect = [0, 0])
    def test_space_for_ship_in_row_returns_location_where_ship_fit_if_there_is_space(self, mock):
        ship_size = 5
        empty_board = self.board_helper.generate_empty_board()
        row_coordinate, column_coordinate = self.place.find_space_in_row(empty_board, ship_size)

        self.assertEqual(row_coordinate, 0)
        self.assertEqual(column_coordinate, 0)
    
    @patch('core.placement.Place.create_random_num', side_effect = [1, 0, 2, 2])
    def test_if_there_is_no_space_in_row_method_loops_until_it_finds_space(self, mock_board_spaces):
        ship_size = 5
        self.board.state = [
                [None, None, None, None, None, None, None, None, None, None],
                ['ship', 'ship', None, 'ship', None, 'ship', None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
            ]

        row_coordinate, column_coordinate = self.place.find_space_in_row(self.board.state, ship_size)
        self.assertEqual(row_coordinate, 2)
        self.assertEqual(column_coordinate, 2)
    
    @patch('core.placement.Place.create_random_num', side_effect = [4, 1])
    def test_space_for_ship_in_column_returns_coordinates_where_ship_fit_when_there_is_space(self, mock_coordinates):
        ship_size = 5
        empty_board = self.board_helper.generate_empty_board()
        row_coordinate, column_coordinate = self.place.find_space_in_column(empty_board, ship_size)

        self.assertEqual(row_coordinate, 4)
        self.assertEqual(column_coordinate, 1)
    
    @patch('core.placement.Place.create_random_num', side_effect = [0, 0, 0, 1])
    def test_if_there_is_no_space_in_column_method_loops_until_it_finds_space(self, mock_coordinates):
        ship_size = 5
        self.board.state = [
                ['ship', None, 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
                ['ship', None, 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
                ['ship', None, 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
                ['ship', None, 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
                ['ship', None, 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
                ['ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
                ['ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
                ['ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
                ['ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
                ['ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ]

        row_coordinate, column_coordinate = self.place.find_space_in_column(self.board.state, ship_size)

        self.assertEqual(row_coordinate, 0)
        self.assertEqual(column_coordinate, 1)
