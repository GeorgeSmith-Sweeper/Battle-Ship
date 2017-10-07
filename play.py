class Game:
    def __init__(self, board, spot_chooser, ui):
        self.ui = ui
        self.board = board
        pass 
    def play(self):
        self.ui.display("Welcome to Battleship")
        self.ui.display(self.board.format())
        pass

class TerminalUi:
    def display(self, message):
       print(message)

class Board:
    def __init__(self):
        self.state = [[None for ele in range(10)] for index in range(10)]

    def format(self):
        formatted_board = ''
        for row in range(0, len(self.state)):
            formatted_board += '\n'
            for column in range(0, len(self.state[row])):
                formatted_board += '[]'
        formatted_board += '\n'
        return formatted_board

class SpotChooser:
    def __init__(self, board):
        pass
    pass

