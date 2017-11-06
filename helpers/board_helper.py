class BoardHelper:
    def __init__(self, all_ships):
        self.all_ships = all_ships
    
    def generate_all_spots(self):
        all_spots_list = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10']
    
        return all_spots_list

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
                [self.all_ships[0], self.all_ships[0], self.all_ships[0], self.all_ships[0], self.all_ships[0], None, None, None, None, self.all_ships[3]], 
                [None, None, None, None, None, None, None, None, None, self.all_ships[3]],
                [None, None, None, None, None, None, None, None, None, self.all_ships[3]],
                [None, None, None, None, self.all_ships[2], None, None, None, None, None],
                [None, self.all_ships[4], None, None, self.all_ships[2], None, None, None, None, None],
                [None, self.all_ships[4], None, None, self.all_ships[2], None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, self.all_ships[1], self.all_ships[1], self.all_ships[1], self.all_ships[1]],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]
        return board_with_ships 

    def generate_board_with_hit(self):
        board_with_a_hit = [
                [self.all_ships[0], 'Hit', self.all_ships[0], self.all_ships[0], self.all_ships[0], None, None, None, None, self.all_ships[3]], 
                [None, None, None, None, None, None, None, None, None, self.all_ships[3]],
                [None, None, None, None, None, None, None, None, None, self.all_ships[3]],
                [None, None, None, None, self.all_ships[2], None, None, None, None, None],
                [None, self.all_ships[4], None, None, self.all_ships[2], None, None, None, None, None],
                [None, self.all_ships[4], None, None, self.all_ships[2], None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, self.all_ships[1], self.all_ships[1], self.all_ships[1], self.all_ships[1]],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]
        return board_with_a_hit
    
    def generate_board_with_a_miss(self):
        board_with_a_miss = [
                [self.all_ships[0], self.all_ships[0], self.all_ships[0], self.all_ships[0], self.all_ships[0], None, None, None, None, self.all_ships[3]], 
                ['Miss', None, None, None, None, None, None, None, None, self.all_ships[3]],
                [None, None, None, None, None, None, None, None, None, self.all_ships[3]],
                [None, None, None, None, self.all_ships[2], None, None, None, None, None],
                [None, self.all_ships[4], None, None, self.all_ships[2], None, None, None, None, None],
                [None, self.all_ships[4], None, None, self.all_ships[2], None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, self.all_ships[1], self.all_ships[1], self.all_ships[1], self.all_ships[1]],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]
        return board_with_a_miss

    def generate_board_with_hit_and_miss(self):
        board_with_hit_and_miss = [
                ['Hit', self.all_ships[0], self.all_ships[0], self.all_ships[0], self.all_ships[0], None, None, None, None, self.all_ships[3]], 
                ['Miss', None, None, None, None, None, None, None, None, self.all_ships[3]],
                [None, None, None, None, None, None, None, None, None, self.all_ships[3]],
                [None, None, None, None, self.all_ships[2], None, None, None, None, None],
                [None, self.all_ships[4], None, None, self.all_ships[2], None, None, None, None, None],
                [None, self.all_ships[4], None, None, self.all_ships[2], None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, self.all_ships[1], self.all_ships[1], self.all_ships[1], self.all_ships[1]],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]
        return board_with_hit_and_miss
    
    def generate_board_with_a_sunken_ship(self):
        board_with_a_sunken_ship = [
                ['Sunk', 'Sunk', 'Sunk', 'Sunk', 'Sunk', None, None, None, None, self.all_ships[3]], 
                [None, None, None, None, None, None, None, None, None, self.all_ships[3]],
                [None, None, None, None, None, None, None, None, None, self.all_ships[3]],
                [None, None, None, None, self.all_ships[2], None, None, None, None, None],
                [None, self.all_ships[4], None, None, self.all_ships[2], None, None, None, None, None],
                [None, self.all_ships[4], None, None, self.all_ships[2], None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, self.all_ships[1], self.all_ships[1], self.all_ships[1], self.all_ships[1]],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                ]
        return board_with_a_sunken_ship
