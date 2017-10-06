from core import board
from core import ui


class Game(ui.BoardPresenter, ui.Messages):
    def __init__(self, board):
        self.board = board

    def start(self):
        self.terminal_msg(self.display_terminal_board(self.board.state)) 

if __name__ == "__main__":
    new_board = board.Board()
    new_game = Game(new_board)
    new_game.start()
