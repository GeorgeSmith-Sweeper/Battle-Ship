from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.board import Board
from core.placement import Place
from core.validate import Validate
from core.ships import Ships
from helpers.board_helper import BoardHelper

class TestBoard(TestCase):

    def setUp(self):
       self.board = Board()
       self.ships = Ships()
       self.board_helper = BoardHelper(self.ships)

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
        self.board.state[0][0] = {
                'name': 'Aircraft Carrier',
                'size': 5,
                'sunk': True,
                'hit_locations': [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],
                }
        shot_result = 'Sunk'
        self.board.update(user_shot_choice, shot_result)

        self.assertEqual(self.board.state, self.board_helper.generate_board_with_a_sunken_ship())
             
    @patch('core.placement.Place.create_random_num', return_value = 0)
    @patch('core.placement.Place.create_random_num', return_value = 0)
    def test_ship_added_to_row_if_there_is_room(self, mock1, mock2):
        place = Place()
        all_ships = [{ 
                'name': 'Aircraft Carrier',
                'size': 5,
                'health': 5,
                'sunk': False,
                }]
        state_after_move = [
                [all_ships[0], all_ships[0], all_ships[0], all_ships[0], all_ships[0], None, None, None, None, None],
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
        self.board.add_to_board(all_ships, place, ship_orientation)

        self.assertEqual(self.board.state, state_after_move)

    @patch('core.placement.Place.create_random_num', return_value = 0)
    @patch('core.placement.Place.create_random_num', return_value = 0)
    def test_ship__added_to_column_if_there_is_room(self, mock1, mock2):
        place = Place()
        all_ships = [{ 
                'name': 'Aircraft Carrier',
                'size': 5,
                'health': 5,
                'sunk': False,
                }]
        state_after_move = [
                [all_ships[0], None, None, None, None, None, None, None, None, None],
                [all_ships[0], None, None, None, None, None, None, None, None, None],
                [all_ships[0], None, None, None, None, None, None, None, None, None],
                [all_ships[0], None, None, None, None, None, None, None, None, None],
                [all_ships[0], None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]
        ship_orientation = 'column'
        self.board.add_to_board(all_ships, place, ship_orientation)

        self.assertEqual(self.board.state, state_after_move)
    
    
