import random 

class Ai: 

    def __init__(self, validate):
        self.validate = validate
        self.col_lets = [chr(i) for i in range(ord('A'), ord('J')+1)]
        self.row_nums = [str(i) for i in range(1, 11)]
        self.all_spots = [(let + num) for let in self.col_lets for num in self.row_nums]
        self.next_shots_list = []


    def get_spot_above(self, letter, number, all_spots, human_board):
        if (self.row_nums.index(number) - 1) >= 0:
            shot_num = self.row_nums[self.row_nums.index(number) - 1]
            spot_above = letter + shot_num
            if spot_above in all_spots:
                return spot_above
    
    def get_spot_below(self, letter, number, all_spots, human_board):
        if (self.row_nums.index(number) + 1) <= len(human_board):
            shot_num = self.row_nums[self.row_nums.index(number) + 1]
            spot_below = letter + shot_num
            if spot_below in all_spots:
                return spot_below
    
    def get_spot_to_left(self, letter, number, all_spots, human_board):
        if (self.col_lets.index(letter) - 1) >= 0:
            shot_letter = self.col_lets[self.col_lets.index(letter) - 1]
            spot_to_left = shot_letter + number 
            if spot_to_left in all_spots:
                return spot_to_left
    
    def get_spot_to_right(self, letter, number, all_spots, human_board):
        if (self.col_lets.index(letter) + 1) <= len(human_board):
            shot_letter = self.col_lets[self.col_lets.index(letter) + 1]
            spot_to_right = shot_letter + number 
            if spot_to_right in all_spots:
                return spot_to_right

    def get_surrounding_spots(self, selected_spot, all_spots, human_board):
        user_letter, user_num = self.validate.split_user_shot(selected_spot)
        spot_above = self.get_spot_above(user_letter, user_num, all_spots, human_board)
        spot_below = self.get_spot_below(user_letter, user_num, all_spots, human_board)
        spot_left = self.get_spot_to_left(user_letter, user_num, all_spots, human_board)
        spot_right = self.get_spot_to_right(user_letter, user_num, all_spots, human_board)
        self.next_shots_list.extend((spot_above, spot_below, spot_left, spot_right))

    def choose_random_spot(self):
        random_index = random.randint(0, len(self.all_spots) - 1)
        random_spot = self.all_spots.pop(random_index)
        return random_spot 

    def shoots_at_board(self, human_board, ui):
        random_spot = self.choose_random_spot()
        shot_result = self.validate.hit_ship(human_board.state, random_spot, human_board.all_ships, ui)
        human_board.update(random_spot, shot_result)

