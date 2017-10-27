from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.ships import Ships
from helpers.board_helper import BoardHelper

class TestBoardHelper(TestCase):
    def setUp(self):
        self.ships = Ships()
        self.board_helper = BoardHelper(self.ships)    

    def test_generate_empty_board_returns_an_empty_board(self):
        empty_board = [
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

        self.assertEqual(self.board_helper.generate_empty_board(), empty_board)
    
    def test_generate_all_occupied_but_one_returns_a_board_with_one_open_spot(self):
        all_occupied_but_one = [
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               [None, 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
              ]

        self.assertEqual(self.board_helper.generate_all_but_one(), all_occupied_but_one)
    
    def test_generate_full_board_returns_a_board_with_all_spots_filled(self):
        full_board = [
                ['Sunk', "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss"],
                ['Sunk', "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss"],
                ['Sunk', "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss"],
                ['Sunk', "Miss", "Miss", "Miss", 'Sunk', "Miss", "Miss", "Miss", "Miss", "Miss"],
                ['Sunk', 'Sunk', "Miss", "Miss", 'Sunk', "Miss", "Miss", "Miss", "Miss", "Miss"],
                ["Miss", 'Sunk', "Miss", "Miss", 'Sunk', "Miss", "Miss", "Miss", "Miss", "Miss"],
                ["Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss"],
                ["Miss", "Miss", "Miss", "Miss", "Miss", "Miss", 'Sunk', 'Sunk', 'Sunk', 'Sunk'],
                ["Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss"],
                ['Sunk', 'Sunk', 'Sunk', "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss"],
              ]
        
        self.assertEqual(self.board_helper.generate_full_board(), full_board)

    def test_generate_board_with_ships_returns_a_board_with_ships(self):
        board_with_ships = [
                [self.ships.all_ships[0], self.ships.all_ships[0], self.ships.all_ships[0], self.ships.all_ships[0], self.ships.all_ships[0], None, None, None, None, self.ships.all_ships[3]], 
                [None, None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1]],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]

        self.assertEqual(self.board_helper.generate_board_with_ships(), board_with_ships)

    def test_generate_board_with_hit_returns_a_board_with_a_hit(self):
        board_with_a_hit = [
                [self.ships.all_ships[0], 'Hit', self.ships.all_ships[0], self.ships.all_ships[0], self.ships.all_ships[0], None, None, None, None, self.ships.all_ships[3]], 
                [None, None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1]],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]

        self.assertEqual(self.board_helper.generate_board_with_hit(), board_with_a_hit)

    def test_generate_board_with_a_miss_returns_a_board_with_a_miss(self):
        board_with_a_miss = [
                [self.ships.all_ships[0], self.ships.all_ships[0], self.ships.all_ships[0], self.ships.all_ships[0], self.ships.all_ships[0], None, None, None, None, self.ships.all_ships[3]], 
                ['Miss', None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1]],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]

        self.assertEqual(self.board_helper.generate_board_with_a_miss(), board_with_a_miss)
    def test_generate_board_with_hit_and_miss_returns_a_board_with_a_hit_and_miss(self):
        board_with_hit_and_miss = [
                ['Hit', self.ships.all_ships[0], self.ships.all_ships[0], self.ships.all_ships[0], self.ships.all_ships[0], None, None, None, None, self.ships.all_ships[3]], 
                ['Miss', None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1]],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]

        self.assertEqual(self.board_helper.generate_board_with_hit_and_miss(), board_with_hit_and_miss)

    def test_generate_board_with_sunken_ship_returns_a_board_with_a_sunken_ship(self):
        board_with_a_sunken_ship = [
                ['Sunk', 'Sunk', 'Sunk', 'Sunk', 'Sunk', None, None, None, None, self.ships.all_ships[3]], 
                [None, None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1]],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]

        self.assertEqual(self.board_helper.generate_board_with_a_sunken_ship(), board_with_a_sunken_ship)
        
        