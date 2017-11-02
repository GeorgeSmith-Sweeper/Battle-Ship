from core import board, ui, validate, ships, placement, ai

class Game:
    def __init__(self, comp_board, human_board, ui, ai, validate, place):
        self.ui = ui
        self.comp_board = comp_board 
        self.human_board = human_board
        self.validate = validate
        self.place = place
        self.ai = ai
        

    def play(self):
        self.ui.display("Welcome to Battleship")
        all_sunk = False
        ship_orientation = 'row'
        self.comp_board.add_to_board(self.place, ship_orientation)

        while not all_sunk:
            self.ui.display("Take your best shot")
            self.ui.display(self.ui.format(self.comp_board.state, self.comp_board.ships.all_ships))
            spot_choice = self.validate.spot_occupied(self.comp_board.state, self.ui, self.comp_board.ships.all_ships)
            shot_result = self.validate.hit_ship(self.comp_board.state, spot_choice, self.comp_board.ships.all_ships, self.ui)
            self.comp_board.update(spot_choice, shot_result)
            all_sunk = self.validate.all_ships_sunk(self.comp_board.state, self.comp_board.ships.all_ships) 
            self.ai.shoots_at_board(self.human_board, self.ui)
            all_sunk = self.validate.all_ships_sunk(self.human_board.state, self.human_board.ships.all_ships) 
            

if __name__ == "__main__":
    ships = ships.Ships()
    comp_board = board.Board(ships)
    human_board = board.Board(ships)
    ui = ui.TerminalUi()
    validate = validate.Validate()
    place = placement.Place()
    ai = ai.Ai(validate)
    game = Game(comp_board, human_board, ai, ui, validate, place)
    game.play()

