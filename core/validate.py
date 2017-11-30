import helpers.constants as consts


class Validate:

    def __init__(self):
        self.col_letters = consts.COL_LETTERS
        self.row_nums = consts.ROW_NUMS
        self.all_spots = consts.ALL_SPOTS
        self.rows = consts.ROWS
        self.columns = consts.COLUMNS

    def split_user_shot(self, shot_choice):
        user_letter = shot_choice[0]
        user_num = shot_choice[1:]
        return user_letter, user_num

    def get_current_spot(self, board_state, user_shot_choice):
        user_letter, user_num = self.split_user_shot(user_shot_choice)
        row = self.rows[user_num]
        column = self.columns[user_letter]
        return board_state[row][column]

    def spot_exists(self, spot):
        return spot in self.all_spots

    def spot_occupied(self, board, spot):
        current_spot = self.get_current_spot(board.state, spot)
        return current_spot is not None and current_spot not in board.all_ships

    def spot_is_legal(self, board, spot):
        if self.spot_exists(spot) is True and self.spot_occupied(board, spot) is False:
            return True
        return False

    def _store_hits(self, current_ship, shot):
        user_letter, user_num = self.split_user_shot(shot)
        row = self.rows[user_num]
        column = self.columns[user_letter]
        current_ship['hit_locations'].append([row, column])
        return current_ship

    def _hit_ship(self, ship, spot_choice):
        current_ship = self._store_hits(ship, spot_choice)
        if self._is_ship_sunk(current_ship):
            return consts.SUNK, current_ship
        return consts.HIT, current_ship

    def _is_ship_sunk(self, current_ship):
        return len(current_ship['hit_locations']) == current_ship['size']

    def shot_result(self, board, user_shot_choice):
        current_spot = self.get_current_spot(board.state, user_shot_choice)
        if current_spot in board.all_ships:
            ship = current_spot
            return self._hit_ship(ship, user_shot_choice)
        return consts.MISS, False

    def all_ships_sunk(self, board):
        all_sunk = True
        for ship in board.all_ships:
            if self._is_ship_sunk(ship) is False:
                return False
        return all_sunk
