class Board:
    def __init__(self):
        self.state = [[None for ele in range(10)] for index in range(10)]
        self.rows = {
                '1': 0,
                '2': 1,
                '3': 2,
                '4': 3,
                '5': 4,
                '6': 5,
                '7': 6,
                '8': 7,
                '9': 8,
                '10': 9,
                }
        self.columns = {
                'A': 0,
                'B': 1,
                'C': 2,
                'D': 3,
                'E': 4,
                'F': 5,
                'G': 6,
                'H': 7,
                'I': 8,
                'J': 9,
                }
    def update(self, user_shot_choice, is_hit):
        user_letter = user_shot_choice[0]
        user_num = user_shot_choice[1:]
        
        self.state[self.rows[user_num]][self.columns[user_letter]] = 'Hit' if is_hit else 'Miss' 
            
    def add_to_board(self, all_ships, place, ship_orientation):
        all_ships_copy = all_ships.copy()
        row_int = place.create_random_num()
        col_int = place.create_random_num()

        while len(all_ships_copy) > 0:
            ship = 0
            if ship_orientation == 'row':

                while place.can_ship_fit_in_row(self.state, all_ships_copy[ship]['size'], row_int, col_int) == False:
                    row_int = place.create_random_num()
                    col_int = place.create_random_num()

                for ele in range(all_ships_copy[ship]['size']):
                    self.state[row_int][ele - (len(self.state) - col_int)] = all_ships_copy[ship]['symbol']
            else:
                while place.can_ship_fit_in_column(self.state, all_ships_copy[ship]['size'], row_int, col_int) == False:
                    row_int = place.create_random_num()
                    col_int = place.create_random_num()

                for ele in range(all_ships_copy[ship]['size']):
                    self.state[ele - (len(self.state) - row_int)][col_int] = all_ships_copy[ship]['symbol']

            all_ships_copy.pop(0)
            ship_orientation = 'column' if ship_orientation == 'row' else 'row'
