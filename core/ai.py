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

    def shoot_at_board(self, board):
        if len(self.next_shots_list) > 0:
            smart_spot = self.next_shots_list.pop()
            return self._computer_shot(board, smart_spot)
        random_spot = self._choose_random_spot()
        return self._computer_shot(board, random_spot)

    def _choose_random_spot(self):
        all_spots_copy = copy.copy(self.all_spots)
        random_index = random.randint(0, len(all_spots_copy) - 1)
        random_spot = all_spots_copy.pop(random_index)
        return random_spot

    def _computer_shot(self, board, spot):
        shot_result, current_ship = self.validate.shot_result(board, spot)
        self._plan_next_moves(shot_result, spot, board)
        board.update(spot, shot_result)
        self._remove_duplicated_spots(spot, self.next_shots_list)
        self._remove_spot_from_choices(spot)
        return shot_result, current_ship

    def _plan_next_moves(self, shot_result, shot_location, board):
        if shot_result == HIT:
            self._get_surrounding_spots(shot_location, board.state)

    def _get_spot(self, row, column, direction, offset, coordinate_method, room_check, board_state):
        if room_check(direction, offset, board_state):
            spot = coordinate_method(row, column, offset)
            spot = self._legal_space(spot)
        else:
            spot = None
        return spot

    def _get_surrounding_spots(self, selected_spot, board_state):
        user_letter, user_num = self.validate.split_user_shot(selected_spot)

        spot_above = self._get_spot(user_num, user_letter, user_num, -1, self._y_axis_spot_coordinates, self._room_from_top_edge, board_state)
        spot_left = self._get_spot(user_num, user_letter, user_letter, -1, self._x_axis_spot_coordinates, self._room_from_left_edge, board_state)
        spot_below = self._get_spot(user_num, user_letter, user_num, 1, self._y_axis_spot_coordinates, self._room_from_bottom_edge, board_state)
        spot_right = self._get_spot(user_num, user_letter, user_letter, 1, self._x_axis_spot_coordinates, self._room_from_right_edge, board_state)

        gathered_spots = list((spot_above, spot_below, spot_left, spot_right))
        self.next_shots_list.extend(self._remove_none_from_list(gathered_spots))

    def _find_index(self, location_list, orientaion, offset):
        return location_list.index(orientaion) + offset

    def _room_from_top_edge(self, row_str, offset, board_state):
        return self._find_index(self.row_nums, row_str, offset) >= 0

    def _room_from_left_edge(self, column_str, offset, board_state):
        return self._find_index(self.col_letters, column_str, offset) >= 0

    def _room_from_bottom_edge(self, row_str, offset, board_state):
        return self._find_index(self.row_nums, row_str, offset) < len(board_state)

    def _room_from_right_edge(self, column_str, offset, board_state):
        return self._find_index(self.col_letters, column_str, offset) < len(board_state)

    def _y_axis_spot_coordinates(self, row_str, column_str, offset):
        return column_str + self.row_nums[self._find_index(self.row_nums, row_str, offset)]

    def _x_axis_spot_coordinates(self, row_str, column_str, offset):
        return self.col_letters[self._find_index(self.col_letters, column_str, offset)] + row_str

    def _legal_space(self, spot):
        if spot in self.all_spots:
            return spot
        return None

    def _remove_none_from_list(self, spots_list):
        return list(filter(lambda ele: ele is not None, spots_list))

    def _remove_duplicated_spots(self, spot_type, shots_list):
        self.next_shots_list = list(filter(lambda spot: spot != spot_type, shots_list))

    def _remove_spot_from_choices(self, spot):
        self.all_spots.pop(self.all_spots.index(spot))
