import helpers.constants as consts


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
        game_over = False
        ship_orientation = 'row'
        self.comp_board.add_to_board(self.place, ship_orientation)
        self.human_board.add_to_board(self.place, ship_orientation)
        # duck typing, instances of terminal_board, boolean comparisons
        while not game_over:
            self._human_turn(self.comp_board)
            if self._is_game_over(self.comp_board, self.ui.HUMAN_WIN_MSG):
                break
            self._computer_turn(self.human_board)
            if self._is_game_over(self.human_board, self.ui.COMP_WIN_MSG):
                break

    def _computer_turn(self, board):
        shot_result, current_ship = self.ai.shoot_at_board(board)
        self.ui.display(self.ui.game_board(self.human_board))
        self.ui.display(self.ui.ship_messages(shot_result, current_ship))

    def _human_turn(self, board):
        self.ui.display(self.ui.game_board(self.comp_board))
        spot = self.ui.get_input(consts.PROMPT)
        while not self.validate.spot_is_legal(board, spot):
            self.ui.display(consts.INVALID_SPOT)
            spot = self.ui.get_input(consts.PROMPT)
        shot_result, current_ship = self.validate.shot_result(board, spot)
        self.ui.display(self.ui.ship_messages(shot_result, current_ship))
        board.update(spot, shot_result)

    def _is_game_over(self, board, message):
        if self.validate.all_ships_sunk(board):
            self.ui.display(message)
            self.ui.display(self.ui.game_board(board))
            return True
        return False
