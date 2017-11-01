class Board:
    def __init__(self, ships):
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
        self.ships = ships

    def update_spot_to_sunk(self, y_coordinate, x_coordinate):
        for each_hit in self.state[y_coordinate][x_coordinate]['hit_locations']:
            row = each_hit[0]
            column = each_hit[1]
            self.state[row][column] = 'Sunk'
    
    def update(self, user_shot_choice, is_hit):
        user_letter = user_shot_choice[0]
        user_num = user_shot_choice[1:]
        y_coordinate = self.rows[user_num]
        x_coordinate = self.columns[user_letter]

        if is_hit == 'Hit':
            self.state[y_coordinate][x_coordinate] = 'Hit' 
        elif is_hit == 'Miss': 
            self.state[y_coordinate][x_coordinate] = 'Miss' 
        else:
            self.update_spot_to_sunk(y_coordinate, x_coordinate)

    def add_to_board(self, place, ship_orientation):
        all_ships_copy = self.ships.all_ships.copy()
        while len(all_ships_copy) > 0:
            ship = 0
            if ship_orientation == 'row':                
                row_int, col_int = place.find_space_in_row(self.state, all_ships_copy[ship]['size'])
                for ele in range(all_ships_copy[ship]['size']):
                    self.state[row_int][ele - (len(self.state) - col_int)] = all_ships_copy[ship]
            else:
                row_int, col_int = place.find_space_in_column(self.state, all_ships_copy[ship]['size'])
                for ele in range(all_ships_copy[ship]['size']):
                    self.state[ele - (len(self.state) - row_int)][col_int] = all_ships_copy[ship]

            all_ships_copy.pop(0)
            ship_orientation = 'column' if ship_orientation == 'row' else 'row'
