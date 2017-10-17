import random

class Place:
    def create_random_num(self):
       num = random.randint(0, 9)
       return num
    
    def can_ship_fit_in_row(self, board_state, ship_size, row_int, col_int):
        if (col_int + ship_size) > len(board_state): return False
        requested_row = board_state[row_int]
        slice_of_row = requested_row[col_int : col_int + (len(requested_row) - ship_size)]
        ship_fits = all([spot == None for spot in slice_of_row])
        return ship_fits

    def can_ship_fit_in_column(self, board_state, ship_size, row_int, col_int):
        if (row_int + ship_size) > len(board_state): return False
        requested_col = [sub_list[col_int] for sub_list in board_state]
        slice_of_col = requested_col[row_int : row_int + (len(requested_col) - ship_size)]
        ship_fits = all([spot == None for spot in slice_of_col])
        return ship_fits


