import random
import copy
from helpers.constants import COL_LETTERS, ROW_NUMS, HIT


class Ai:

    def __init__(self, validate):
        self.validate = validate
        self.col_letters = COL_LETTERS
        self.row_nums = ROW_NUMS
        self.all_spots = [(letter + num) for letter in self.col_letters for num in self.row_nums]
        self.next_shots_list = []

    def _room_from_top_edge(self, row):
        return (self.row_nums.index(row) - 1) >= 0

    def _room_from_left_edge(self, column):
        return (self.col_letters.index(column) - 1) >= 0

    def _room_from_bottom_edge(self, row, human_board_state):
        return (self.row_nums.index(row) + 1) < len(human_board_state)

    def _room_from_right_edge(self, column, human_board_state):
        return (self.col_letters.index(column) + 1) < len(human_board_state)

    def _top_spot_coordinates(self, row, column, offset):
        return column + self.row_nums[self.row_nums.index(row) - offset]

    def _bottom_spot_coordinates(self, row, column, offset):
        return column + self.row_nums[self.row_nums.index(row) + offset]

    def _left_spot_coordinates(self, row, column, offset):
        return self.col_letters[self.col_letters.index(column) - offset] + row

    def _right_spot_coordinates(self, row, column, offset):
        return self.col_letters[self.col_letters.index(column) + offset] + row

    def _legal_space(self, spot):
        if spot in self.all_spots:
            return spot
        return None

    def _get_spot_above(self, column, row):
        if self._room_from_top_edge(row):
            spot_above = self._top_spot_coordinates(row, column, 1)
            return self._legal_space(spot_above)
        return None

    def _get_spot_to_left(self, column, row):
        if self._room_from_left_edge(column):
            spot_to_left = self._left_spot_coordinates(row, column, 1)
            return self._legal_space(spot_to_left)
        return None

    def _get_spot_below(self, column, row, human_board_state):
        if self._room_from_bottom_edge(row, human_board_state):
            return self._legal_space(self._bottom_spot_coordinates(row, column, 1))
        return self._legal_space(self._bottom_spot_coordinates(row, column, 0))

    def _get_spot_to_right(self, column, row, human_board_state):
        if self._room_from_right_edge(column, human_board_state):
            return self._legal_space(self._right_spot_coordinates(row, column, 1))
        return self._legal_space(self._right_spot_coordinates(row, column, 0))

    def _remove_none_from_list(self, spots_list):
        return list(filter(lambda ele: ele is not None, spots_list))

    def _get_surrounding_spots(self, selected_spot, human_board_state):
        user_letter, user_num = self.validate.split_user_shot(selected_spot)
        spot_above = self._get_spot_above(user_letter, user_num)
        spot_left = self._get_spot_to_left(user_letter, user_num)
        spot_below = self._get_spot_below(user_letter, user_num, human_board_state)
        spot_right = self._get_spot_to_right(user_letter, user_num, human_board_state)
        gathered_spots = list((spot_above, spot_below, spot_left, spot_right))
        self.next_shots_list.extend(self._remove_none_from_list(gathered_spots))

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

    def _computer_shot(self, human_board, spot):
        shot_result, current_ship = self.validate.shot_result(human_board, spot)
        self._plan_next_moves(shot_result, spot, human_board)
        human_board.update(spot, shot_result)
        self._remove_duplicated_spots(spot, self.next_shots_list)
        self._remove_spot_from_choices(spot)
        return shot_result, current_ship

    def shoot_at_board(self, human_board):
        if len(self.next_shots_list) > 0:
            smart_spot = self.next_shots_list.pop()
            return self._computer_shot(human_board, smart_spot)
        random_spot = self._choose_random_spot()
        return self._computer_shot(human_board, random_spot)
