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
            shot_result, current_ship = self.human_turn(self.comp_board)
            self.ui.display(self.ui.ship_messages(shot_result, current_ship))
            all_sunk = self.validate.all_ships_sunk(self.comp_board)
            if all_sunk is True:
                self.ui.display(self.ui.HUMAN_WIN_MSG)
                self.ui.display(self.ui.terminal_board(self.comp_board))
                break
            shot_result, current_ship = self.computer_turn(self.human_board)
            self.ui.display(self.ui.ship_messages(shot_result, current_ship))
            self.ui.display(self.ui.terminal_board(self.human_board))
            all_sunk = self.validate.all_ships_sunk(self.human_board)
            if all_sunk is True:
                self.ui.display(self.ui.COMP_WIN_MSG)
                self.ui.display(self.ui.terminal_board(self.human_board))
                break

    def computer_turn(self, board):
        shot_result, current_ship = self.ai.shoot_at_board(board)
        return shot_result, current_ship

    def human_turn(self, board):
        spot = self.ui.get_input('>>')
        while self.validate.spot_is_legal(board, spot) is False:
            spot = self.ui.get_input('That spot is invalid. Pick a new location')

        shot_result, current_ship = self.validate.shot_result(board, spot)
        board.update(spot, shot_result)
        return shot_result, current_ship
