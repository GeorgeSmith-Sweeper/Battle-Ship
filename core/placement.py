import random


class Place:
    def create_random_num(self):
        random_num = random.randint(0, 9)
        return random_num

    def find_space_in_row(self, board_state, ship_size, result=''):
        ship_fits = result
        while ship_fits is not True:
            row_int = self.create_random_num()
            col_int = self.create_random_num()
            requested_row = board_state[row_int]
            slice_of_row = requested_row[row_int: row_int + (len(requested_row) - ship_size)]
            ship_fits = all([spot is None for spot in slice_of_row])
            if (col_int + ship_size) > len(board_state):
                ship_fits = False
        return row_int, col_int

    def find_space_in_column(self, board_state, ship_size, result=''):
        ship_fits = result
        while ship_fits is not True:
            row_int = self.create_random_num()
            col_int = self.create_random_num()
            requested_col = [sub_list[col_int] for sub_list in board_state]
            slice_of_col = requested_col[row_int: row_int + (len(requested_col) - ship_size)]
            ship_fits = all([spot is None for spot in slice_of_col])
            if (row_int + ship_size) > len(board_state):
                ship_fits = False
        return row_int, col_int
