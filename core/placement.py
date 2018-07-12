import random


class Place:

    def find_space_for_ship(self, board_state, ship_size, orientation, result=''):
        ship_fits = result
        while not ship_fits:
            row_int, col_int = self._get_random_row_and_column(board_state)
            requested_location = self._location_type(orientation, row_int, col_int, board_state)
            slice_of_location = self._location_for_ship(requested_location, row_int, ship_size)
            open_spaces = self._are_spaces_open(slice_of_location)
            ship_fits = self._ship_fits(row_int, col_int, ship_size, board_state, open_spaces, orientation)
        return row_int, col_int

    def _get_random_row_and_column(self, board_state):
        row = random.randint(0, (len(board_state) - 1))
        column = random.randint(0, (len(board_state) - 1))
        return row, column

    def _location_type(self, orientation, row_int, col_int, board_state):
        if orientation == 'row':
            return self._get_row(row_int, board_state)
        return self._get_column(col_int, board_state)

    def _get_row(self, row_int, board_state):
        return board_state[row_int]

    def _get_column(self, col_int, board_state):
        return [sub_list[col_int] for sub_list in board_state]

    def _location_for_ship(self, requested_location, row_int, ship_size):
        return requested_location[row_int: row_int + (len(requested_location) - ship_size)]

    def _are_spaces_open(self, location):
        return all([spot is None for spot in location])

    def _ship_over_edge(self, ship_start, ship_size, board_state, open_spaces):
        if (ship_start + ship_size) > len(board_state):
            return False
        return open_spaces

    def _ship_fits(self, row_int, col_int, ship_size, board_state, open_spaces, orientation):
        if orientation == 'row':
            return self._ship_over_edge(col_int, ship_size, board_state, open_spaces)
        return self._ship_over_edge(row_int, ship_size, board_state, open_spaces)