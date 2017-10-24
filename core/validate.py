class Validate:
    def __init__(self):
        self.col_lets = [chr(i) for i in range(ord('A'), ord('J')+1)]
        self.row_nums = [str(i) for i in range(1, 11)]
        self.all_spots = [(let + num) for let in self.col_lets for num in self.row_nums]
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
                '10': 9
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
                'J': 9
                }
    
    def split_user_shot(self, shot_choice):
        user_let = shot_choice[0]
        user_num = shot_choice[1:]
        return user_let, user_num

    def board_full(self, board_state):
        full = True
        for row in range(0, len(board_state)):
            for ele in board_state[row]:
                if ele is None:
                    return False
        return full

    def spot_exists(self, ui):
        user_shot_choice = ui.get_input('>>')

        while user_shot_choice not in self.all_spots:
            ui.display('Spot does not exist, Try again')
            user_shot_choice = ui.get_input('>>')
        return user_shot_choice

    def spot_occupied(self, board_state, ui, all_ships):
        ship_symbols = ui.get_ship_symbols(all_ships) 
        user_shot_choice = self.spot_exists(ui)
        user_let, user_num = self.split_user_shot(user_shot_choice)
            
        while board_state[self.rows[user_num]][self.columns[user_let]] is not None and board_state[self.rows[user_num]][self.columns[user_let]] not in ship_symbols: 
            ui.display('That spot is occupied. Pick a different spot')
            user_shot_choice = self.spot_exists(ui)
            user_let, user_num = self.split_user_shot(user_shot_choice)
        return user_shot_choice
   

    def hit_ship(self, board_state, shot, all_ships, ui):
        user_let, user_num = self.split_user_shot(shot)
        for ship in range(len(all_ships)):
            if board_state[self.rows[user_num]][self.columns[user_let]] == all_ships[ship]['symbol']:
                all_ships[ship] = self.reduce_ship_health(all_ships[ship])
                ui.display('You hit the ' + all_ships[ship]['name'] + '!')
                return True
        ui.display('Miss!')
        return False
    
    def reduce_ship_health(self, current_ship):
        current_ship['health'] -= 1
        return current_ship

    def is_ship_sunk(self, current_ship):
        is_sunk = True if current_ship['health'] <= 0 else False
        return is_sunk
