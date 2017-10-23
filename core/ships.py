import random

class Ships:
    def __init__(self):
        self.aircraft_carrier = {
                'name': 'Aircraft Carrier',
                'symbol': 'AC',
                'size': 5,
                'health': 5,
                }
        self.battleship = {
                'name': 'Battleship',
                'symbol': 'B',
                'size': 4,
                'health': 4,
                }
        self.cruiser = {
                'name': 'Cruiser',
                'symbol': 'C',
                'size': 3,
                'health': 3,
                }
        self.submarine = {
                'name': 'Submarine',
                'symbol': 'S',
                'size': 3,
                'health': 3,
                }
        self.destroyer = {
                'name': 'Destroyer',
                'symbol': 'D',
                'size': 2,
                'health': 2,
                }
        self.all_ships = [
                self.aircraft_carrier, 
                self.battleship, 
                self.cruiser,
                self.submarine,
                self.destroyer,
                ]
