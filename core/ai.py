import random 

class Ai: 
    def __init__(self, validate):
        self.validate = validate
        self.col_lets = [chr(i) for i in range(ord('A'), ord('J')+1)]
        self.row_nums = [str(i) for i in range(1, 11)]
        self.all_spots = [(let + num) for let in self.col_lets for num in self.row_nums]
        
    def choose_random_spot(self):
        random_index = random.randint(0, len(self.all_spots) - 1)
        random_spot = self.all_spots.pop(random_index)
        return random_spot 

    def shoots_at_board(self, human_board, ui):
        random_spot = self.choose_random_spot()
        shot_result = self.validate.hit_ship(human_board.state, random_spot, human_board.ships.all_ships, ui)
        human_board.update(random_spot, shot_result)

