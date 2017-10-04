from core import board
from core import ui 

if __name__ == "__main__":
    current_board = board.Board()
    board = ui.BoardPresenter()
    message = ui.Messages()
    message.terminal_msg(board.display_terminal_board(current_board.state))
    
