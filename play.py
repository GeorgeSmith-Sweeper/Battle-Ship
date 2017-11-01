from core import board, ui, validate, ships, placement

class Game:
    def __init__(self, board, ui, validate, place):
        self.ui = ui
        self.board = board
        self.validate = validate
        self.place = place

    def play(self):
        self.ui.display("Welcome to Battleship")
        board_full = False
        ship_orientation = 'row'
        self.board.add_to_board(self.board.ships.all_ships, self.place, ship_orientation)

        while not board_full:
            self.ui.display("Take your best shot")
            self.ui.display(self.ui.format(self.board.state, self.board.ships.all_ships))
            spot_choice = self.validate.spot_occupied(self.board.state, self.ui, self.board.ships.all_ships)
            shot_result = self.validate.hit_ship(self.board.state, spot_choice, self.board.ships.all_ships, self.ui)
            self.board.update(spot_choice, shot_result)
            board_full = self.validate.board_full(self.board.state) 


if __name__ == "__main__":
    ships = ships.Ships()
    board = board.Board(ships)
    ui = ui.TerminalUi()
    validate = validate.Validate()
    place = placement.Place()
    game = Game(board, ui, validate, place)
    game.play()

