import helpers.constants as constants


class Validate:

    def __init__(self):
        self.col_lets = constants.COL_LETS
        self.row_nums = constants.ROW_NUMS
        self.all_spots = constants.ALL_SPOTS
        self.rows = constants.ROWS
        self.columns = constants.COLUMNS

    def split_user_shot(self, shot_choice):
        user_let = shot_choice[0]
        user_num = shot_choice[1:]
        return user_let, user_num

    def get_current_spot(self, board_state, user_shot_choice):
        user_let, user_num = self.split_user_shot(user_shot_choice)
        row = self.rows[user_num]
        column = self.columns[user_let]
        return board_state[row][column]

    def spot_exists(self, ui):
        user_shot_choice = ui.get_input('>>')

        while user_shot_choice not in self.all_spots:
            ui.display('Spot does not exist, Try again')
            user_shot_choice = ui.get_input('>>')
        return user_shot_choice

    def spot_occupied(self, board, ui):
        user_shot_choice = self.spot_exists(ui)
        current_spot = self.get_current_spot(board.state, user_shot_choice)

        while current_spot is not None and current_spot not in board.all_ships:
            ui.display('That spot is occupied. Pick a different spot')
            user_shot_choice = self.spot_exists(ui)
            current_spot = self.get_current_spot(board.state, user_shot_choice)
        return user_shot_choice

    def hit_ship(self, board, spot_choice, ui):
        current_spot = self.get_current_spot(board.state, spot_choice)
        for ship in range(len(board.all_ships)):
            if current_spot == board.all_ships[ship]:
                board.all_ships[ship] = self.store_hits(board.all_ships[ship], spot_choice)
                if self.is_ship_sunk(board.all_ships[ship], ui):
                    return constants.SUNK
                ui.display('You hit the ' + board.all_ships[ship]['name'] + '!')
                return constants.HIT
        ui.display('Miss!')
        return constants.MISS

    def store_hits(self, current_ship, shot):
        user_let, user_num = self.split_user_shot(shot)
        row = self.rows[user_num]
        column = self.columns[user_let]

        current_ship['hit_locations'].append([row, column])
        return current_ship

    def is_ship_sunk(self, current_ship, ui):
        if len(current_ship['hit_locations']) == current_ship['size']:
            ui.display("You sunk the " + current_ship['name'] + '!')
            return True
        return False

    def all_ships_sunk(self, board):
        all_sunk = True
        for row in range(0, len(board.state)):
            for ele in board.state[row]:
                if ele in board.all_ships:
                    return False
        return all_sunk
