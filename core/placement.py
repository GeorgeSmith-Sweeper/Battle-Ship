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
    '''
    def _open_and_proper_size(self, loc_slice, start, ship_size, board_state):
        spaces_open = self._are_spaces_open(loc_slice)
        too_long = self._is_ship_too_long(start, ship_size, board_state)
        if too_long is True:
            return False
        if spaces_open is True:
            return True
    '''
    def _location_for_ship(self, requested_location, row_int, ship_size):
        return requested_location[row_int: row_int + (len(requested_location) - ship_size)]

    def find_space_in_row(self, board_state, ship_size, result=''):
        ship_fits = result
        while ship_fits is not True:
            row_int, col_int = self.get_random_row_and_column(board_state)
            requested_row = board_state[row_int]
            slice_of_row = self._location_for_ship(requested_row, row_int, ship_size)
            ship_fits = self._are_spaces_open(slice_of_row)
            ship_fits = self._ship_over_edge(col_int, ship_size, board_state, ship_fits)
            '''
            ship_fits = self._open_and_proper_size(slice_of_row, col_int, ship_size, board_state)
            '''
        return row_int, col_int

    def find_space_in_column(self, board_state, ship_size, result=''):
        ship_fits = result
        while ship_fits is not True:
            row_int, col_int = self.get_random_row_and_column(board_state)
            requested_col = [sub_list[col_int] for sub_list in board_state]
            slice_of_col = self._location_for_ship(requested_col, row_int, ship_size)
            ship_fits = self._are_spaces_open(slice_of_col)
            ship_fits = self._ship_over_edge(row_int, ship_size, board_state, ship_fits)
            '''
            ship_fits = self._open_and_proper_size(slice_of_col, row_int, ship_size, board_state)
            '''
        return row_int, col_int
