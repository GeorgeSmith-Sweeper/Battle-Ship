class Messages:
    def terminal_msg(self, item_to_print):
        print(item_to_print)

class BoardPresenter:
    def display_terminal_board(self, board):
         board_string = ''
         for row in range(0, len(board)):
             board_string += '\n'
             for column in range(0, len(board[row])):
                board_string += '[]'
         board_string += '\n'
         return board_string
