import copy
from helpers.constants import ROWS, COLUMNS, HIT, MISS, SUNK


class Board:

    def __init__(self):
        self.state = [[None for ele in range(10)] for index in range(10)]
        self.rows = ROWS
        self.columns = COLUMNS
        self.aircraft_carrier = {
            'name': 'Aircraft Carrier',
            'size': 5,
            'hit_locations': [],
        }
        self.battleship = {
            'name': 'Battleship',
            'size': 4,
            'hit_locations': [],
        }
        self.cruiser = {
            'name': 'Cruiser',
            'size': 3,
            'hit_locations': [],
        }
        self.submarine = {
            'name': 'Submarine',
            'size': 3,
            'hit_locations': [],
        }
        self.destroyer = {
            'name': 'Destroyer',
            'size': 2,
            'hit_locations': [],
        }
        self.all_ships = [
            self.aircraft_carrier,
            self.battleship,
            self.cruiser,
            self.submarine,
            self.destroyer,
        ]

    def update_spot_to_sunk(self, y_coordinate, x_coordinate):
        for each_hit in self.state[y_coordinate][x_coordinate]['hit_locations']:
            row = each_hit[0]
            column = each_hit[1]
            self.state[row][column] = SUNK

    def update(self, user_shot_choice, shot_result):
        user_letter = user_shot_choice[0]
        user_num = user_shot_choice[1:]
        y_coordinate = self.rows[user_num]
        x_coordinate = self.columns[user_letter]

        if shot_result == HIT:
            self.state[y_coordinate][x_coordinate] = HIT
        elif shot_result == MISS:
            self.state[y_coordinate][x_coordinate] = MISS
        else:
            self.update_spot_to_sunk(y_coordinate, x_coordinate)

    def add_ship_to_row(self, ship, all_ships_copy, place):
        row_int, col_int = place.find_space_in_row(self.state, all_ships_copy[ship]['size'])
        for ele in range(all_ships_copy[ship]['size']):
            self.state[row_int][ele - (len(self.state) - col_int)] = all_ships_copy[ship]

    def add_ship_to_column(self, ship, all_ships_copy, place):
        row_int, col_int = place.find_space_in_column(self.state, all_ships_copy[ship]['size'])
        for ele in range(all_ships_copy[ship]['size']):
            self.state[ele - (len(self.state) - row_int)][col_int] = all_ships_copy[ship]

    def add_to_board(self, place, ship_orientation):
        all_ships_copy = copy.copy(self.all_ships)
        orientation = ship_orientation
        for ship in range(len(all_ships_copy)):
            if orientation == 'row':
                self.add_ship_to_row(ship, all_ships_copy, place)
            else:
                self.add_ship_to_column(ship, all_ships_copy, place)
            orientation = 'column' if orientation == 'row' else 'row'
