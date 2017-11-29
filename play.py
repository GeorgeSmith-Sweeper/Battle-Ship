from core import board, ui, validate, placement, ai

class Game:
    def __init__(self, comp_board, human_board, ai, ui, validate, place):
        self.ai = ai
        self.ui = ui
        self.comp_board = comp_board 
        self.human_board = human_board
        self.validate = validate
        self.place = place
        
    def play(self):
        self.ui.display(self.ui.WELCOME_MSG)
        self.ui.display(self.ui.INSTRUCTIONS)
        all_sunk = False
        ship_orientation = 'row'
        self.comp_board.add_to_board(self.place, ship_orientation)
        self.human_board.add_to_board(self.place, ship_orientation)

        while not all_sunk:
            self.ui.display(self.ui.terminal_board(self.comp_board))
            spot_choice = self.validate.spot_occupied(self.comp_board, self.ui)
            shot_result = self.validate.hit_ship(self.comp_board, spot_choice, self.ui)
            self.comp_board.update(spot_choice, shot_result)
            all_sunk = self.validate.all_ships_sunk(self.comp_board) 
            if all_sunk == True:
                self.ui.display(self.ui.HUMAN_WIN_MSG)
                break

            self.ai.shoots_at_board(self.human_board, self.ui)
            self.ui.display(self.ui.terminal_board(self.human_board))
            all_sunk = self.validate.all_ships_sunk(self.human_board) 
            if all_sunk == True:
                self.ui.display(self.ui.COMP_WIN_MSG)
                break
            
if __name__ == "__main__":
    comp_board = board.Board()
    human_board = board.Board()
    ui = ui.TerminalUi()
    validate = validate.Validate()
    place = placement.Place()
    ai = ai.Ai(validate)
    game = Game(comp_board, human_board, ai, ui, validate, place)
    game.play()

