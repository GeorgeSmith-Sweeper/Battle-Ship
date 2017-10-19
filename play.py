from core import board, ui, validate, ships, placement

class Game:
    def __init__(self, board, ui, validate, ships, place):
        self.ui = ui
        self.board = board
        self.validate = validate
        self.ships = ships
        self.place = place

    def play(self):
        self.ui.display("Welcome to Battleship")
        board_full = False
        ship_orientation = 'row'
        self.board.add_to_board(self.ships.all_ships, self.place, ship_orientation)

        while not board_full:
            board_full = self.validate.board_full(self.board.state) 
            self.ui.display("Take your best shot")
            self.ui.display(self.ui.format(self.board.state, self.ships.all_ships))
            spot_choice = self.validate.spot_occupied(self.board.state, self.ui, self.ships.all_ships)
            hit = self.validate.hit_ship(self.board.state, spot_choice, self.ships.all_ships, self.ui)
            self.board.update(spot_choice, hit)


if __name__ == "__main__":
    board = board.Board()
    ui = ui.TerminalUi()
    validate = validate.Validate()
    ships = ships.Ships()
    place = placement.Place()
    game = Game(board, ui, validate, ships, place)
    game.play()

