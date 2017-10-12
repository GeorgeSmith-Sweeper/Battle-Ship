from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.board import Board
from core.ships import Ships

class TestShips(TestCase):
    def test_ships_is_initialized_with_a_five_unique_ships(self):
        ships = Ships()
        aircraft_carrier_symbol = 'AC' 
        battleship_symbol = 'B'
        cruiser_symbol = 'C'
        submarine_symbol = 'S'
        destroyer_symbol = 'D'

        self.assertEqual(ships.aircraft_carrier['symbol'], aircraft_carrier_symbol)
        self.assertEqual(ships.destroyer['symbol'], destroyer_symbol)
        self.assertEqual(ships.cruiser['symbol'], cruiser_symbol)
        self.assertEqual(ships.submarine['symbol'], submarine_symbol)
        self.assertEqual(ships.battleship['symbol'], battleship_symbol)

    def test_each_ship_has_a_size(self):
        ships = Ships()
        aircraft_carrier_size = 5
        battleship_size = 4
        cruiser_size = 3
        submarine_size = 3
        destroyer_size = 2

        self.assertEqual(ships.aircraft_carrier['size'], aircraft_carrier_size)
        self.assertEqual(ships.battleship['size'], battleship_size)
        self.assertEqual(ships.cruiser['size'], cruiser_size)
        self.assertEqual(ships.submarine['size'], submarine_size)
        self.assertEqual(ships.destroyer['size'], destroyer_size)
    
    def test_create_random_generates_a_num_from_0_to_9(self):
        ships = Ships()
        board = Board()
        zero_to_nine_list = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]
        random_num = ships.create_random_num()
        self.assertIn(random_num,  zero_to_nine_list)
    
    '''
    def test_place_on_board__places_ships_on_an_empty_board(self):
        ships = Ships()
        board = Board()

        board_with_ships = [
               ['AC', 'AC', 'AC', 'AC','AC', None, None, None, None, None],
               ['B', 'B', 'B', 'B', None, None, None, None, None, None],
               ['C', 'C', 'C', None, None, None, None, None, None, None],
               ['S', 'S', 'S', None, None, None, None, None, None, None],
               ['D', 'D', None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
            ]
        
        self.assertEqual(ships.place_on_board(board.state), board_with_ships)
    
    
    def test_is_column_empty_returns_true_if_there_is_enough_space_for_ship(self):
        ships = Ships()
        board = Board()
        column_num = 3
        ship_size = 5

        board_with_ships = [
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
        
        self.assertEqual(ships.room_in_column(board_with_ships, column_num, ship_size), True)  
    '''
