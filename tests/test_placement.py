from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.board import Board
from core.ships import Ships
from core.placement import Place

class TestPlace(TestCase):
    def setUp(self):
        self.board = Board()
        self.place = Place()
        self.ships = Ships()
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

    def test_create_random_generates_a_num_from_0_to_9(self):
        zero_to_nine_list = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]
        random_num = self.place.create_random_num()
        self.assertIn(random_num,  zero_to_nine_list)

    def test_space_for_ship_in_row_returns_True_if_there_is_space(self):
        col_int = 0
        row_int = 0
        ship_size = 5
        result = self.place.can_ship_fit_in_row(self.empty_board, ship_size, row_int, col_int)

        self.assertEqual(result, True)

    def test_space_for_ship_in_row_returns_True_if_there_is_space_2nd(self):
        col_int = 0
        row_int = 4
        ship_size = 5
        result = self.place.can_ship_fit_in_row(self.empty_board, ship_size, row_int, col_int)

        self.assertEqual(result, True)

    def test_space_for_ship_in_row_returns_False_if_there_is_no_space(self):
        col_int = 0
        row_int = 1
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

        result = self.place.can_ship_fit_in_row(self.board.state, ship_size, row_int, col_int)
        self.assertEqual(result, False)

    def test_space_for_ship_in_column_returns_True_if_there_is_space(self):
        col_int = 1
        row_int = 4
        ship_size = 5
        result = self.place.can_ship_fit_in_column(self.empty_board, ship_size, row_int, col_int)

        self.assertEqual(result, True)

    def test_space_for_ship_in_column_returns_False_if_there_is_no_space(self):
        col_int = 0
        row_int = 7
        ship_size = 5
        self.board.state = [
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ['ship', None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ['ship', None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
            ]

        result = self.place.can_ship_fit_in_column(self.board.state, ship_size, row_int, col_int)
        self.assertEqual(result, False)
