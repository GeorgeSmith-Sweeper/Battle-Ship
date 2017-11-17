import helpers.constants as consts


class Validate:

    def __init__(self):
        self.col_lets = consts.COL_LETS
        self.row_nums = consts.ROW_NUMS
        self.all_spots = consts.ALL_SPOTS
        self.rows = consts.ROWS
        self.columns = consts.COLUMNS

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
            ui.display(consts.DOES_NOT_EXIST_MSG)
            user_shot_choice = ui.get_input('>>')
        return user_shot_choice

    def spot_occupied(self, board, ui):
        user_shot_choice = self.spot_exists(ui)
        current_spot = self.get_current_spot(board.state, user_shot_choice)
        while current_spot is not None and current_spot not in board.all_ships:
            ui.display(consts.OCCUPIED_MSG)
            user_shot_choice = self.spot_exists(ui)
            current_spot = self.get_current_spot(board.state, user_shot_choice)
        return user_shot_choice

    # Test
    def hit_ship(self, ship, spot_choice):
        current_ship = self.store_hits(ship, spot_choice)
        if self.is_ship_sunk(current_ship):
            return consts.SUNK, current_ship
        return consts.HIT, current_ship

    def shot_result(self, board, user_shot_choice):
        current_spot = self.get_current_spot(board.state, user_shot_choice)
        if current_spot in board.all_ships:
            ship = current_spot
            return self.hit_ship(ship, user_shot_choice)
        return consts.MISS, False

    def store_hits(self, current_ship, shot):
        user_let, user_num = self.split_user_shot(shot)
        row = self.rows[user_num]
        column = self.columns[user_let]
        current_ship['hit_locations'].append([row, column])
        return current_ship

    def is_ship_sunk(self, current_ship):
        if len(current_ship['hit_locations']) == current_ship['size']:
            return True
        return False

    def all_ships_sunk(self, board):
        all_sunk = True
        for row in board.state:
            for ele in row:
                if ele in board.all_ships:
                    return False
        return all_sunk
