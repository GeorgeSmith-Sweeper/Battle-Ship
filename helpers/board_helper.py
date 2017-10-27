class BoardHelper:
    def __init__(self, ships):
        self.ships = ships

    def generate_empty_board(self):
       empty_board = [
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None, None, None],
               ]
       return empty_board  
    
    def generate_all_but_one(self):
        all_occupied_but_one = [
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               [None, 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
               ['Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss', 'Miss'],
              ]
        return all_occupied_but_one

    def generate_full_board(self):
        full_board = [
                ['Sunk', "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss"],
                ['Sunk', "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss"],
                ['Sunk', "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss"],
                ['Sunk', "Miss", "Miss", "Miss", 'Sunk', "Miss", "Miss", "Miss", "Miss", "Miss"],
                ['Sunk', 'Sunk', "Miss", "Miss", 'Sunk', "Miss", "Miss", "Miss", "Miss", "Miss"],
                ["Miss", 'Sunk', "Miss", "Miss", 'Sunk', "Miss", "Miss", "Miss", "Miss", "Miss"],
                ["Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss"],
                ["Miss", "Miss", "Miss", "Miss", "Miss", "Miss", 'Sunk', 'Sunk', 'Sunk', 'Sunk'],
                ["Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss"],
                ['Sunk', 'Sunk', 'Sunk', "Miss", "Miss", "Miss", "Miss", "Miss", "Miss", "Miss"],
              ]
        return full_board

    def generate_board_with_ships(self):
        board_with_ships = [
                [self.ships.all_ships[0], self.ships.all_ships[0], self.ships.all_ships[0], self.ships.all_ships[0], self.ships.all_ships[0], None, None, None, None, self.ships.all_ships[3]], 
                [None, None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1]],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]
        return board_with_ships 

    def generate_board_with_hit(self):
        board_with_a_hit = [
                [self.ships.all_ships[0], 'Hit', self.ships.all_ships[0], self.ships.all_ships[0], self.ships.all_ships[0], None, None, None, None, self.ships.all_ships[3]], 
                [None, None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1]],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]
        return board_with_a_hit
    
    def generate_board_with_a_miss(self):
        board_with_a_miss = [
                [self.ships.all_ships[0], self.ships.all_ships[0], self.ships.all_ships[0], self.ships.all_ships[0], self.ships.all_ships[0], None, None, None, None, self.ships.all_ships[3]], 
                ['Miss', None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1]],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]
        return board_with_a_miss
    
    def generate_board_with_a_sunken_ship(self):
        board_with_a_sunken_ship = [
                ['Sunk', 'Sunk', 'Sunk', 'Sunk', 'Sunk', None, None, None, None, self.ships.all_ships[3]], 
                [None, None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, None, None, None, None, None, self.ships.all_ships[3]],
                [None, None, None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, self.ships.all_ships[4], None, None, self.ships.all_ships[2], None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1], self.ships.all_ships[1]],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]
        return board_with_a_sunken_ship
