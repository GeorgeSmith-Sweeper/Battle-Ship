from unittest import TestCase
from unittest.mock import patch
from core.board import Board
from core.placement import Place
from helpers.board_helper import BoardHelper


class TestBoard(TestCase):

    def setUp(self):
        self.board = Board()
        self.board_helper = BoardHelper(self.board.all_ships)

    def test_all_ships_contains_all_5_ships(self):
        self.assertEqual(len(self.board.all_ships), 5)

    def test_each_ship_has_a_hit_location_array(self):
        hit_locations = []

        self.assertEqual(self.board.aircraft_carrier['hit_locations'], hit_locations)
        self.assertEqual(self.board.destroyer['hit_locations'], hit_locations)
        self.assertEqual(self.board.cruiser['hit_locations'], hit_locations)
        self.assertEqual(self.board.submarine['hit_locations'], hit_locations)
        self.assertEqual(self.board.battleship['hit_locations'], hit_locations)

    def test_each_ship_has_a_size(self):
        aircraft_carrier_size = 5
        battleship_size = 4
        cruiser_size = 3
        submarine_size = 3
        destroyer_size = 2

        self.assertEqual(self.board.aircraft_carrier['size'], aircraft_carrier_size)
        self.assertEqual(self.board.battleship['size'], battleship_size)
        self.assertEqual(self.board.cruiser['size'], cruiser_size)
        self.assertEqual(self.board.submarine['size'], submarine_size)
        self.assertEqual(self.board.destroyer['size'], destroyer_size)

    def test_each_ship_has_a_name(self):
        aircraft_carrier_name = 'Aircraft Carrier'
        battleship_name = 'Battleship'
        cruiser_name = 'Cruiser'
        submarine_name = 'Submarine'
        destroyer_name = 'Destroyer'

        self.assertEqual(self.board.aircraft_carrier['name'], aircraft_carrier_name)
        self.assertEqual(self.board.battleship['name'], battleship_name)
        self.assertEqual(self.board.cruiser['name'], cruiser_name)
        self.assertEqual(self.board.submarine['name'], submarine_name)
        self.assertEqual(self.board.destroyer['name'], destroyer_name)

    def test_Hit_is_added_to_board_if_the_user_hit_a_ship(self):
        user_shot_choice = 'B1'
        self.board.state = self.board_helper.generate_board_with_ships()
        shot_result = 'Hit'
        self.board.update(user_shot_choice, shot_result)

        self.assertEqual(self.board.state, self.board_helper.generate_board_with_hit())

    def test_Miss_is_added_to_board_if_the_user_Misses_a_ship(self):
        user_shot_choice = 'A2'
        self.board.state = self.board_helper.generate_board_with_ships()
        shot_result = 'Miss'
        self.board.update(user_shot_choice, shot_result)

        self.assertEqual(self.board.state, self.board_helper.generate_board_with_a_miss())

    def test_when_ship_sinks_all_positions_where_ship_was_are_updated_to_str_Sunk(self):
        user_shot_choice = 'A1'
        self.board.state = self.board_helper.generate_board_with_ships()
        row = 0
        column = 0
        self.board.state[row][column] = {
            'name': 'Aircraft Carrier',
            'size': 5,
            'sunk': True,
            'hit_locations': [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],
        }
        shot_result = 'Sunk'
        self.board.update(user_shot_choice, shot_result)

        self.assertEqual(self.board.state, self.board_helper.generate_board_with_a_sunken_ship())

    @patch('core.placement.Place._get_random_row_and_column', side_effect=[(0, 0)])
    def test_a_ship_is_added_to_row_if_there_is_room(self, mock_coordinates):
        place = Place()
        self.board.all_ships = [{
            'name': 'Aircraft Carrier',
            'size': 5,
            'hit_locations': [],
        }]
        state_after_move = [
            [self.board.all_ships[0], self.board.all_ships[0], self.board.all_ships[0], self.board.all_ships[0], self.board.all_ships[0], None, None, None, None, None],
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
        ship_orientation = 'row'
        self.board.add_to_board(place, ship_orientation)

        self.assertEqual(self.board.state, state_after_move)

    @patch('core.placement.Place._get_random_row_and_column', side_effect=[(0, 0)])
    def test_ship__added_to_column_if_there_is_room(self, mock_coordinates):
        place = Place()
        self.board.all_ships = [{
            'name': 'Aircraft Carrier',
            'size': 5,
            'hit_locations': [],
        }]
        state_after_move = [
            [self.board.all_ships[0], None, None, None, None, None, None, None, None, None],
            [self.board.all_ships[0], None, None, None, None, None, None, None, None, None],
            [self.board.all_ships[0], None, None, None, None, None, None, None, None, None],
            [self.board.all_ships[0], None, None, None, None, None, None, None, None, None],
            [self.board.all_ships[0], None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
        ]
        ship_orientation = 'column'
        self.board.add_to_board(place, ship_orientation)
        self.maxDiff = None

        self.assertEqual(self.board.state, state_after_move)
