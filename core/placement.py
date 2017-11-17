import random


class Place:

    def create_random_num(self, board_state):
        random_num = random.randint(0, len(board_state) - 1)
        return random_num

    def get_random_row_and_column(self, board_state):
        row_int = self.create_random_num(board_state)
        col_int = self.create_random_num(board_state)
        return row_int, col_int

    def _are_spaces_open(self, location):
        return all([spot is None for spot in location])

    def _is_ship_too_long(self, start, ship_size, board_state):
        if (start + ship_size) > len(board_state):
            return False
        return True

    def _location_for_ship(self, requested_location, row_int, ship_size):
        return requested_location[row_int: row_int + (len(requested_location) - ship_size)]

    def find_space_in_row(self, board_state, ship_size):
        ship_fits = ''
        while ship_fits is not True:
            row_int, col_int = self.get_random_row_and_column(board_state)
            requested_row = board_state[row_int]
            slice_of_row = self._location_for_ship(requested_row, row_int, ship_size)
            ship_fits = self._is_ship_too_long(col_int, ship_size, board_state)
            ship_fits = self._are_spaces_open(slice_of_row)
        return row_int, col_int

    def find_space_in_column(self, board_state, ship_size):
        ship_fits = ''
        while ship_fits is not True:
            row_int, col_int = self.get_random_row_and_column(board_state)
            requested_col = [sub_list[col_int] for sub_list in board_state]
            slice_of_col = self._location_for_ship(requested_col, row_int, ship_size)
            ship_fits = self._is_ship_too_long(row_int, ship_size, board_state)
            ship_fits = self._are_spaces_open(slice_of_col)
        return row_int, col_int
