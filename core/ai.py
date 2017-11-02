import random 

class Ai: 
    def __init__(self, validate):
        self.validate = validate

    def choose_random_spot(self):
        all_spots = self.validate.all_spots
        random_spot = all_spots.pop(random.randint(0, len(all_spots) - 1))
        return random_spot 

    def shoots_at_board(self, human_board, ui):
        random_spot = self.choose_random_spot()
        human_board.update(random_spot, self.validate.hit_ship(human_board.state, random_spot, human_board.ships.all_ships, ui))

