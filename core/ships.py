import random

class Ships:
    def __init__(self):
        self.aircraft_carrier = {
                'symbol': 'AC',
                'size': 5,
                }
        self.battleship = {
                'symbol': 'B',
                'size': 4,
                }
        self.cruiser = {
                'symbol': 'C',
                'size': 3
                }
        self.submarine = {
                'symbol': 'S',
                'size': 3,
                }
        self.destroyer = {
                'symbol': 'D',
                'size': 2,
                }
        self.all_ships = [
                self.aircraft_carrier, 
                self.battleship, 
                self.cruiser,
                self.submarine,
                self.destroyer,
                ]
