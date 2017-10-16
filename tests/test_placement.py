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

    def test_create_random_generates_a_num_from_0_to_9(self):
        zero_to_nine_list = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]
        random_num = self.place.create_random_num()
        self.assertIn(random_num,  zero_to_nine_list)

    def test_ship_fit_calls_row_fit_check_when_orientation_is_row(self):
        self.place.can_ship_fit_in_row = MagicMock()
        ship_orientation = 'row'
        ship_size = 5
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
        self.place.ship_fit(self.board.state, ship_size, ship_orientation)

        self.place.can_ship_fit_in_row.assert_called()

    def test_space_for_ship_in_row_returns_location_if_there_is_space(self):
        col_int = 0
        row_int = 0
        ship_size = 5
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

        legal_ship_location = {
                'start': 0,
                'end': 5,
                }
        result = self.place.can_ship_fit_in_row(self.board.state, ship_size, row_int, col_int)
        self.assertEqual(result, legal_ship_location)

    def test_space_for_ship_in_row_returns_location_if_there_is_space_2nd(self):
        col_int = 0
        row_int = 4
        ship_size = 5
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

        legal_ship_location = {
                'start': 0,
                'end': 5,
                }
        result = self.place.can_ship_fit_in_row(self.board.state, ship_size, row_int, col_int)
        self.assertEqual(result, legal_ship_location)

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

    def test_space_for_ship_in_column_returns_location_if_there_is_space(self):
        col_int = 1
        row_int = 4 
        ship_size = 5
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

        legal_ship_location = {
                'start': 4,
                'end': 9,
                }
        result = self.place.can_ship_fit_in_column(self.board.state, ship_size, row_int, col_int)
        self.assertEqual(result, legal_ship_location)
