from unittest import TestCase
from unittest.mock import patch
from core.board import Board
from core.placement import Place
from helpers.board_helper import BoardHelper


class TestPlace(TestCase):
    def setUp(self):
        self.board = Board()
        self.place = Place()
        self.board_helper = BoardHelper(self.board.all_ships)
        self.zero_to_nine_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.empty_board = self.board_helper.generate_empty_board()

    def test_get_random_row_and_column_returns_numbers_within_board_size(self):
        row, column = self.place.get_random_row_and_column(self.empty_board)
        self.assertIn(row, self.zero_to_nine_list)
        self.assertIn(column, self.zero_to_nine_list)

    @patch('core.placement.Place.get_random_row_and_column', side_effect=[(0, 0)])
    def test_space_for_ship_in_row_returns_location_where_ship_fit_if_there_is_space(self, mock):
        ship_size = 5
        orientation = 'row'
        row_coordinate, column_coordinate = self.place.find_space_for_ship(self.empty_board, ship_size, orientation)

        self.assertEqual(row_coordinate, 0)
        self.assertEqual(column_coordinate, 0)

    @patch('core.placement.Place.get_random_row_and_column', side_effect=[(1, 0), (2, 2)])
    def test_if_there_is_no_space_in_row_method_loops_until_it_finds_space(self, mock_board_spaces):
        ship_size = 5
        orientation = 'row'
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

        row_coordinate, column_coordinate = self.place.find_space_for_ship(self.board.state, ship_size, orientation)
        self.assertEqual(row_coordinate, 2)
        self.assertEqual(column_coordinate, 2)

    @patch('core.placement.Place.get_random_row_and_column', side_effect=[(4, 1)])
    def test_space_for_ship_in_column_returns_coordinates_where_ship_fit_when_there_is_space(self, mock_coordinates):
        ship_size = 5
        orientation = 'column'
        row_coordinate, column_coordinate = self.place.find_space_for_ship(self.empty_board, ship_size, orientation)

        self.assertEqual(row_coordinate, 4)
        self.assertEqual(column_coordinate, 1)

    @patch('core.placement.Place.get_random_row_and_column', side_effect=[(0, 0), (0, 2)])
    def test_if_there_is_no_space_in_column_method_loops_until_it_finds_space(self, mock_coordinates):
        ship_size = 5
        orientation = 'column'
        self.board.state = [
            ['ship', 'ship', None, 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', None, 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', None, 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', None, 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', None, 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
        ]

        row_coordinate, column_coordinate = self.place.find_space_for_ship(self.board.state, ship_size, orientation)

        self.assertEqual(row_coordinate, 0)
        self.assertEqual(column_coordinate, 2)

    @patch('core.placement.Place.get_random_row_and_column', side_effect=[(0, 2), (0, 3)])
    def test_if_ships_will_not_hang_off_the_edge(self, mock_coordinates):
        ship_size = 5
        orientation = 'column'
        self.board.state = [
            ['ship', 'ship', None, None, 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', None, None, 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', None, None, 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', None, None, 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', 'ship', None, 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
            ['ship', 'ship', None, 'ship', 'ship', 'ship', 'ship', 'ship', 'ship', 'ship'],
        ]

        row_coordinate, column_coordinate = self.place.find_space_for_ship(self.board.state, ship_size, orientation)

        self.assertEqual(row_coordinate, 0)
        self.assertEqual(column_coordinate, 3)
