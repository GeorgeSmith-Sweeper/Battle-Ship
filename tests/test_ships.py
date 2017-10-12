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

    
