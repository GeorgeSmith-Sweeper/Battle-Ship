import random

class Ships:
    def __init__(self):
        self.aircraft_carrier = {
                'name': 'Aircraft Carrier',
                'size': 5,
                'sunk': False,
                'hit_locations': [],
                }
        self.battleship = {
                'name': 'Battleship',
                'size': 4,
                'sunk': False,
                'hit_locations': [],
                }
        self.cruiser = {
                'name': 'Cruiser',
                'size': 3,
                'sunk': False,
                'hit_locations': [],
                }
        self.submarine = {
                'name': 'Submarine',
                'size': 3,
                'sunk': False,
                'hit_locations': [],
                }
        self.destroyer = {
                'name': 'Destroyer',
                'size': 2,
                'sunk': False,
                'hit_locations': [],
                }
        self.all_ships = [
                self.aircraft_carrier, 
                self.battleship, 
                self.cruiser,
                self.submarine,
                self.destroyer,
                ]
