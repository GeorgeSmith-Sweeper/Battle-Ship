import random 
import copy

class Ai: 

    def __init__(self, validate):
        self.validate = validate
        self.col_lets = [chr(i) for i in range(ord('A'), ord('J')+1)]
        self.row_nums = [str(i) for i in range(1, 11)]
        self.all_spots = [(let + num) for let in self.col_lets for num in self.row_nums]
        self.next_shots_list = []


    def get_spot_above(self, letter, number, human_board):
        if (self.row_nums.index(number) - 1) >= 0:
            shot_num = self.row_nums[self.row_nums.index(number) - 1]
            spot_above = letter + shot_num
            if spot_above in self.all_spots:
                return spot_above
    
    def get_spot_below(self, letter, number, human_board):
        if (self.row_nums.index(number) + 1) <= len(human_board):
            shot_num = self.row_nums[self.row_nums.index(number) + 1]
            spot_below = letter + shot_num
            if spot_below in self.all_spots:
                return spot_below
    
    def get_spot_to_left(self, letter, number, human_board):
        if (self.col_lets.index(letter) - 1) >= 0:
            shot_letter = self.col_lets[self.col_lets.index(letter) - 1]
            spot_to_left = shot_letter + number 
            if spot_to_left in self.all_spots:
                return spot_to_left
    
    def get_spot_to_right(self, letter, number, human_board):
        if (self.col_lets.index(letter) + 1) <= len(human_board):
            shot_letter = self.col_lets[self.col_lets.index(letter) + 1]
            spot_to_right = shot_letter + number 
            if spot_to_right in self.all_spots:
                return spot_to_right

    def get_surrounding_spots(self, selected_spot, human_board):
        user_letter, user_num = self.validate.split_user_shot(selected_spot)
        spot_above = self.get_spot_above(user_letter, user_num, human_board)
        spot_below = self.get_spot_below(user_letter, user_num, human_board)
        spot_left = self.get_spot_to_left(user_letter, user_num, human_board)
        spot_right = self.get_spot_to_right(user_letter, user_num, human_board)
        gathered_spots = [spot_above, spot_left, spot_below, spot_right]
        for ele in gathered_spots:
            if ele != None:
                self.next_shots_list.append(ele)

    def choose_random_spot(self):
        all_spots_copy = copy.copy(self.all_spots)
        random_index = random.randint(0, len(all_spots_copy) - 1)
        random_spot = all_spots_copy.pop(random_index)
        return random_spot 

    def intelligent_shot(self, human_board, ui):
        smart_spot = self.next_shots_list.pop()
        shot_result = self.validate.hit_ship(human_board.state, smart_spot, human_board.all_ships, ui)
          
        if shot_result == 'Hit':
            self.get_surrounding_spots(smart_spot, human_board.state)
        human_board.update(smart_spot, shot_result)
        self.all_spots.pop(self.all_spots.index(smart_spot))
    
    def random_shot(self, human_board, ui):
        random_spot = self.choose_random_spot()
        shot_result = self.validate.hit_ship(human_board.state, random_spot, human_board.all_ships, ui)
                
        if shot_result == 'Hit':
            self.get_surrounding_spots(random_spot, human_board.state)
        human_board.update(random_spot, shot_result)
        self.all_spots.pop(self.all_spots.index(random_spot))
    
    def shoots_at_board(self, human_board, ui):
        if len(self.next_shots_list) > 0:
            self.intelligent_shot(human_board, ui)
        else: 
            self.random_shot(human_board, ui)
