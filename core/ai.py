import random 
import copy
import helpers.constants as constants

class Ai: 

    def __init__(self, validate):
        self.validate = validate
        self.col_lets = constants.COL_LETS 
        self.row_nums = constants.ROW_NUMS 
        self.all_spots = [(let + num) for let in self.col_lets for num in self.row_nums]
        self.next_shots_list = []

    def get_spot_above(self, column, row):
        if (self.row_nums.index(row) - 1) >= 0:
            shot_row = self.row_nums[self.row_nums.index(row) - 1]
            spot_above = column + shot_row
            if spot_above in self.all_spots:
                return spot_above
    
    def get_spot_to_left(self, column, row):
        if (self.col_lets.index(column) - 1) >= 0:
            shot_column = self.col_lets[self.col_lets.index(column) - 1]
            spot_to_left = shot_column + row 
            if spot_to_left in self.all_spots:
                return spot_to_left
    
    def get_spot_below(self, column, row, human_board_state):
        spot_below = ""
        if (self.row_nums.index(row) + 1) < len(human_board_state):
            shot_num = self.row_nums[self.row_nums.index(row) + 1]
            spot_below = column + shot_num
        else:
            spot_below = column + row
        if spot_below in self.all_spots:
            return spot_below
    
    def get_spot_to_right(self, column, row, human_board_state):
        spot_to_right = ""
        if (self.col_lets.index(column) + 1) < len(human_board_state):
            shot_column = self.col_lets[self.col_lets.index(column) + 1]
            spot_to_right = shot_column + row 
        else: 
            shot_column = self.col_lets[self.col_lets.index(column)]
            spot_to_right = shot_column + row  
        if spot_to_right in self.all_spots:
            return spot_to_right

    def remove_none_from_list(self, spots_list):
        list_without_nones = list(filter(lambda ele: ele != None, spots_list))
        return list_without_nones
        
    def get_surrounding_spots(self, selected_spot, human_board_state):
        user_letter, user_num = self.validate.split_user_shot(selected_spot)
        spot_above = self.get_spot_above(user_letter, user_num)
        spot_left = self.get_spot_to_left(user_letter, user_num)
        spot_below = self.get_spot_below(user_letter, user_num, human_board_state)
        spot_right = self.get_spot_to_right(user_letter, user_num, human_board_state)
        gathered_spots = [spot_above, spot_below, spot_left, spot_right]
        self.next_shots_list.extend(self.remove_none_from_list(gathered_spots))

    def choose_random_spot(self):
        all_spots_copy = copy.copy(self.all_spots)
        random_index = random.randint(0, len(all_spots_copy) - 1)
        random_spot = all_spots_copy.pop(random_index)
        return random_spot 

    def intelligent_shot(self, human_board, ui):
        print(self.next_shots_list)
        smart_spot = self.next_shots_list.pop()
        shot_result = self.validate.hit_ship(human_board, smart_spot, ui)
          
        if shot_result == 'Hit':
            self.get_surrounding_spots(smart_spot, human_board.state)
        human_board.update(smart_spot, shot_result)
        self.next_shots_list = list(filter(lambda spot: spot != smart_spot, self.next_shots_list))
        self.all_spots.pop(self.all_spots.index(smart_spot))

    def random_shot(self, human_board, ui):
        random_spot = self.choose_random_spot()
        shot_result = self.validate.hit_ship(human_board, random_spot, ui)
                
        if shot_result == 'Hit':
            self.get_surrounding_spots(random_spot, human_board.state)
        human_board.update(random_spot, shot_result)
        self.next_shots_list = list(filter(lambda spot: spot != random_spot, self.next_shots_list))
        self.all_spots.pop(self.all_spots.index(random_spot))
    
    def shoots_at_board(self, human_board, ui):
        if len(self.next_shots_list) > 0:
            self.intelligent_shot(human_board, ui)
        else: 
            self.random_shot(human_board, ui)
