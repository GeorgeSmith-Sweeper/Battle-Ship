from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.board import Board
from core.ships import Ships

class TestShips(TestCase):
    def test_all_ships_contains_all_5_ships(self):
        ships = Ships()
        self.assertEqual(len(ships.all_ships), 5)

    def test_each_ship_has_a_sunk_boolean_that_is_False(self):
        ships = Ships()
        aircraft_carrier_sunk = False
        battleship_sunk = False
        cruiser_sunk = False
        submarine_sunk = False
        destroyer_sunk = False

        self.assertEqual(ships.aircraft_carrier['sunk'], aircraft_carrier_sunk)
        self.assertEqual(ships.destroyer['sunk'], destroyer_sunk)
        self.assertEqual(ships.cruiser['sunk'], cruiser_sunk)
        self.assertEqual(ships.submarine['sunk'], submarine_sunk)
        self.assertEqual(ships.battleship['sunk'], battleship_sunk)

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

    def test_each_ship_has_a_name(self):
        ships = Ships()
        aircraft_carrier_name = 'Aircraft Carrier'
        battleship_name = 'Battleship'
        cruiser_name = 'Cruiser'
        submarine_name = 'Submarine'
        destroyer_name = 'Destroyer'

        self.assertEqual(ships.aircraft_carrier['name'], aircraft_carrier_name)
        self.assertEqual(ships.battleship['name'], battleship_name)
        self.assertEqual(ships.cruiser['name'], cruiser_name)
        self.assertEqual(ships.submarine['name'], submarine_name)
        self.assertEqual(ships.destroyer['name'], destroyer_name)

    def test_each_ship_has_a_health(self):
        ships = Ships()
        aircraft_carrier_health = 5
        battleship_health = 4
        cruiser_health = 3
        submarine_health = 3
        destroyer_health = 2

        self.assertEqual(ships.aircraft_carrier['health'], aircraft_carrier_health)
        self.assertEqual(ships.battleship['health'], battleship_health)
        self.assertEqual(ships.cruiser['health'], cruiser_health)
        self.assertEqual(ships.submarine['health'], submarine_health)
        self.assertEqual(ships.destroyer['health'], destroyer_health)

