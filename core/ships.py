import random

class Ships:
    def __init__(self):
        self.aircraft_carrier = {
                'name': 'Aircraft Carrier',
                'size': 5,
                'health': 5,
                'sunk': False,
                }
        self.battleship = {
                'name': 'Battleship',
                'size': 4,
                'health': 4,
                'sunk': False,
                }
        self.cruiser = {
                'name': 'Cruiser',
                'size': 3,
                'health': 3,
                'sunk': False,
                }
        self.submarine = {
                'name': 'Submarine',
                'size': 3,
                'health': 3,
                'sunk': False,
                }
        self.destroyer = {
                'name': 'Destroyer',
                'size': 2,
                'health': 2,
                'sunk': False,
                }
        self.all_ships = [
                self.aircraft_carrier, 
                self.battleship, 
                self.cruiser,
                self.submarine,
                self.destroyer,
                ]
