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
            user_spot = self.validate.spot_occupied(self.comp_board, self.ui)
            shot_result, current_ship = self.validate.shot_result(self.comp_board, user_spot, self.ui)
            self.comp_board.update(user_spot, shot_result)
            self.ui.display(self.ui.ship_messages(shot_result, current_ship))
            all_sunk = self.validate.all_ships_sunk(self.comp_board)

            if all_sunk is True:
                self.ui.display(self.ui.HUMAN_WIN_MSG)
                break

            self.ai.shoots_at_board(self.human_board, self.ui)
            self.ui.display(self.ui.terminal_board(self.human_board))
            all_sunk = self.validate.all_ships_sunk(self.human_board)

            if all_sunk is True:
                self.ui.display(self.ui.COMP_WIN_MSG)
                break
