import random


class Place:

    def create_random_num(self, board_state):
        random_num = random.randint(0, (len(board_state) - 1))
        return random_num

    def get_random_row_and_column(self, board_state):
        row_int = self.create_random_num(board_state)
        col_int = self.create_random_num(board_state)
        return row_int, col_int

    def _are_spaces_open(self, location):
        return all([spot is None for spot in location])

    def _ship_over_edge(self, ship_start, ship_size, board_state, open_spaces):
        if (ship_start + ship_size) > len(board_state):
            return False
        return open_spaces

    def _location_for_ship(self, requested_location, row_int, ship_size):
        return requested_location[row_int: row_int + (len(requested_location) - ship_size)]

    def _get_row(self, row_int, board_state):
        return board_state[row_int]

    def _get_column(self, col_int, board_state):
        return [sub_list[col_int] for sub_list in board_state]

    def find_space_in_row(self, board_state, ship_size, result=''):
        ship_fits = result
        while ship_fits is not True:
            row_int, col_int = self.get_random_row_and_column(board_state)
            requested_row = self._get_row(row_int, board_state)
            slice_of_row = self._location_for_ship(requested_row, row_int, ship_size)
            open_spaces = self._are_spaces_open(slice_of_row)
            ship_fits = self._ship_over_edge(col_int, ship_size, board_state, open_spaces)
        return row_int, col_int

    def find_space_in_column(self, board_state, ship_size, result=''):
        ship_fits = result
        while ship_fits is not True:
            row_int, col_int = self.get_random_row_and_column(board_state)
            requested_col = self._get_column(col_int, board_state)
            slice_of_col = self._location_for_ship(requested_col, row_int, ship_size)
            open_spaces = self._are_spaces_open(slice_of_col)
            ship_fits = self._ship_over_edge(row_int, ship_size, board_state, open_spaces)
        return row_int, col_int
    ########
    '''
    def find_space_for_ship(self, board_state, ship_size, orientation, result=''):
        ship_fits = result
        requested_location = ""
        while ship_fits is not True:
            row_int, col_int = self.get_random_row_and_column(board_state)
            if orientation == 'row':
                requested_location = self._get_row(row_int, board_state)
            else:
                requested_location = self._get_column(col_int, board_state)
            slice_of_location = self._location_for_ship(requested_location, row_int, ship_size)
            open_spaces = self._are_spaces_open(slice_of_location)
            ship_fits = self._ship_over_edge(row_int, ship_size, board_state, open_spaces)
        return row_int, col_int
    '''
