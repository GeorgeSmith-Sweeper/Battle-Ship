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

    def add_to_board(self, place, ship_orientation):
        orientation = ship_orientation
        for ship in self.all_ships:
            self._add_ship(orientation, ship, place)
            orientation = 'column' if orientation == 'row' else 'row'

    def update(self, user_shot_choice, shot_result):
        user_letter = user_shot_choice[0]
        user_num = user_shot_choice[1:]
        y_coordinate = self.rows[user_num]
        x_coordinate = self.columns[user_letter]

        if shot_result == HIT:
            self._update_spot_to_hit(y_coordinate, x_coordinate)
        if shot_result == MISS:
            self._update_spot_to_miss(y_coordinate, x_coordinate)
        if shot_result == SUNK:
            self._update_spot_to_sunk(y_coordinate, x_coordinate)

    def _update_spot_to_sunk(self, y_coordinate, x_coordinate):
        for each_hit in self.state[y_coordinate][x_coordinate]['hit_locations']:
            row = each_hit[0]
            column = each_hit[1]
            self.state[row][column] = SUNK

    def _update_spot_to_hit(self, y_coordinate, x_coordinate):
        self.state[y_coordinate][x_coordinate] = HIT

    def _update_spot_to_miss(self, y_coordinate, x_coordinate):
        self.state[y_coordinate][x_coordinate] = MISS

    def _add_ship_to_row(self, ship, row_int, col_int):
        for ele in range(ship['size']):
            self.state[row_int][ele - (len(self.state) - col_int)] = ship

    def _add_ship_to_column(self, ship, row_int, col_int):
        for ele in range(ship['size']):
            self.state[ele - (len(self.state) - row_int)][col_int] = ship

    def _add_ship(self, orientation, ship, place):
        row_int, col_int = place.find_space_for_ship(self.state, ship['size'], orientation)
        if orientation == 'row':
            self._add_ship_to_row(ship, row_int, col_int)
        else:
            self._add_ship_to_column(ship, row_int, col_int)
