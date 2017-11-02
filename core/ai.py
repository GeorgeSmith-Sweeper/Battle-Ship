import random 

class Ai: 
    def __init__(self, validate):
        self.validate = validate

    def choose_random_spot(self):
        random_index = random.randint(0, len(self.validate.all_spots) - 1)
        random_spot = self.validate.all_spots.pop(random_index)
        return random_spot 

    def shoots_at_board(self, human_board, ui):
        random_spot = self.choose_random_spot()
        shot_result = self.validate.hit_ship(human_board.state, random_spot, human_board.ships.all_ships, ui)
        human_board.update(random_spot, shot_result)

