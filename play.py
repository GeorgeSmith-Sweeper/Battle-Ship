from core import board, ui, validate, ships

class Game:
    def __init__(self, board, ui, validate, ships):
        self.ui = ui
        self.board = board
        self.validate = validate
        self.ships = ships

    def play(self):
        self.ui.display("Welcome to Battleship")
        board_full = False
        self.ships.place_on_board(self.board.state)
        while not board_full:
            board_full = self.validate.board_full(self.board.state)
            self.ui.display("Take your best shot")
            self.ui.display(self.board.format())
            spot_choice = self.validate.spot_occupied(self.board.state, self.ui)
            self.board.update(spot_choice)


if __name__ == "__main__":
    board = board.Board()
    ui = ui.TerminalUi()
    validate = validate.Validate()
    ships = ships.Ships()
    game = Game(board, ui, validate, ships)
    game.play()

