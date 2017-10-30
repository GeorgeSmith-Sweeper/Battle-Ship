from unittest import TestCase, mock
from unittest.mock import patch, MagicMock
from core.board import Board
from core.ships import Ships

class TestShips(TestCase):
    def test_all_ships_contains_all_5_ships(self):
        ships = Ships()
        self.assertEqual(len(ships.all_ships), 5)

    def test_each_ship_has_a_hit_location_array(self):
        ships = Ships()
        hit_locations = []

        self.assertEqual(ships.aircraft_carrier['hit_locations'], hit_locations)
        self.assertEqual(ships.destroyer['hit_locations'], hit_locations)
        self.assertEqual(ships.cruiser['hit_locations'], hit_locations)
        self.assertEqual(ships.submarine['hit_locations'], hit_locations)
        self.assertEqual(ships.battleship['hit_locations'], hit_locations)

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

        self.assertEqual(ships.cruiser['name'], cruiser_name)
        self.assertEqual(ships.submarine['name'], submarine_name)
        self.assertEqual(ships.destroyer['name'], destroyer_name)


