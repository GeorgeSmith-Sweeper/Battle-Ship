import random
import copy
from helpers.constants import COL_LETS, ROW_NUMS, HIT


class Ai:

    def __init__(self, validate):
        self.validate = validate
        self.col_lets = COL_LETS
        self.row_nums = ROW_NUMS
        self.all_spots = [(let + num) for let in self.col_lets for num in self.row_nums]
        self.next_shots_list = []

    def room_from_top_edge(self, row):
        return (self.row_nums.index(row) - 1) >= 0

    def room_from_left_edge(self, column):
        return (self.col_lets.index(column) - 1) >= 0

    def room_from_bottom_edge(self, row, human_board_state):
        return (self.row_nums.index(row) + 1) < len(human_board_state)

    def room_from_right_edge(self, column, human_board_state):
        return (self.col_lets.index(column) + 1) < len(human_board_state)

    def top_spot_coordinates(self, row, column, offset):
        return column + self.row_nums[self.row_nums.index(row) - offset]

    def left_spot_coordinates(self, row, column, offset):
        return self.col_lets[self.col_lets.index(column) - offset] + row

    def bottom_spot_coordinates(self, row, column, offset):
        return column + self.row_nums[self.row_nums.index(row) + offset]

    def right_spot_coordinates(self, row, column, offset):
        return self.col_lets[self.col_lets.index(column) + offset] + row

    def _legal_space(self, spot):
        if spot in self.all_spots:
            return spot

    def _get_spot_above(self, column, row):
        if (self.row_nums.index(row) - 1) >= 0:
            spot_above = self.top_spot_coordinates(row, column, 1)
            return self._legal_space(spot_above)

    def _get_spot_to_left(self, column, row):
        if self.room_from_left_edge(column):
            spot_to_left = self.left_spot_coordinates(row, column, 1)
            return self._legal_space(spot_to_left)

    def _get_spot_below(self, column, row, human_board_state):
        if self.room_from_bottom_edge(row, human_board_state):
            return self._legal_space(self.bottom_spot_coordinates(row, column, 1))
        return self._legal_space(self.bottom_spot_coordinates(row, column, 0))

    def _get_spot_to_right(self, column, row, human_board_state):
        if self.room_from_right_edge(column, human_board_state):
            return self._legal_space(self.right_spot_coordinates(row, column, 1))
        return self._legal_space(self.right_spot_coordinates(row, column, 0))

    def remove_none_from_list(self, spots_list):
        return list(filter(lambda ele: ele is not None, spots_list))

    def _get_surrounding_spots(self, selected_spot, human_board_state):
        user_letter, user_num = self.validate.split_user_shot(selected_spot)
        spot_above = self._get_spot_above(user_letter, user_num)
        spot_left = self._get_spot_to_left(user_letter, user_num)
        spot_below = self._get_spot_below(user_letter, user_num, human_board_state)
        spot_right = self._get_spot_to_right(user_letter, user_num, human_board_state)
        gathered_spots = list((spot_above, spot_below, spot_left, spot_right))
        self.next_shots_list.extend(self.remove_none_from_list(gathered_spots))

    def _choose_random_spot(self):
        all_spots_copy = copy.copy(self.all_spots)
        random_index = random.randint(0, len(all_spots_copy) - 1)
        random_spot = all_spots_copy.pop(random_index)
        return random_spot

    def _remove_duplicated_spots(self, spot_type, shots_list):
        self.next_shots_list = list(filter(lambda spot: spot != spot_type, shots_list))

    def _remove_spot_from_choices(self, spot):
        self.all_spots.pop(self.all_spots.index(spot))

    def _plan_next_moves(self, shot_result, shot_location, human_board):
        if shot_result == HIT:
            self._get_surrounding_spots(shot_location, human_board.state)

    def _unified_shot(self, human_board, spot):
        shot_result, current_ship = self.validate.shot_result(human_board, spot)
        self._plan_next_moves(shot_result, spot, human_board)
        human_board.update(spot, shot_result)
        self._remove_duplicated_spots(spot, self.next_shots_list)
        self._remove_spot_from_choices(spot)
        return shot_result, current_ship

    def shoots_at_board(self, human_board):
        if len(self.next_shots_list) > 0:
            smart_spot = self.next_shots_list.pop()
            return self._unified_shot(human_board, smart_spot)
        random_spot = self._choose_random_spot()
        return self._unified_shot(human_board, random_spot)
