import random

class Place:
    def create_random_num(self):
       num = random.randint(0, 9)
       return num

    def can_ship_fit_in_row(self, board_state, ship_size, row_int, col_int):
        for col in range(0, len(board_state[row_int]) - ship_size):
            is_None = all([ele == None for ele in board_state[row_int][0 + col: ship_size + col]])
            if is_None == True:
                legal_ship_location = {
                        'start': col,
                        'end': ship_size + col,
                        }
                return legal_ship_location
        return False

    def ship_fit(self, board_state, ship_size, ship_orientation):
        row_int = self.create_random_num()
        col_int = self.create_random_num()
        if ship_orientation == 'row':
           ship_location = self.can_ship_fit_in_row(board_state, ship_size, row_int, col_int)


'''
def can_ship_fit_in_column(self, board_state, ship_size, row_int, col_int):
    for row in range(0, len(board_state[col_int]))
'''
