class TerminalUi:

    def __init__(self):
        self.REDBGCOLOR = '\033[41m'
        self.ENDCOLOR = '\033[0m'
        self.MAGENTA = '\033[35m'
        self.CYAN = '\033[36m'
        self.COMP_WIN_MSG = 'The Computer has sunk all the ships! Game Over!'
        self.HUMAN_WIN_MSG = 'Congratulations, you\'ve has sunk all the computers ships! Game Over!'

    def display(self, message):
       print(message)

    def get_input(self, prompt_string):
        response = input(prompt_string)
        return response

    def add_row_number(self, row_int, total_rows):
        if (row_int + 1) < total_rows:
            return ' ' + str(row_int + 1) + ' '
        else:
            return str(row_int + 1) + ' '
    
    def add_shot_marker(self, board, row, column):
        if board.state[row][column] is None or board.state[row][column] in board.all_ships:
            return '[ ]'
        if board.state[row][column] == 'Miss': 
            return '[' + self.MAGENTA + 'M' + self.ENDCOLOR + ']'
        if board.state[row][column] == 'Hit':
            return '[' + self.CYAN + 'H' + self.ENDCOLOR + ']'
        if board.state[row][column] == 'Sunk':
            return self.REDBGCOLOR + '[S]' + self.ENDCOLOR

    def format(self, board):
        formatted_board = '\n' + '    A  B  C  D  E  F  G  H  I  J'
        
        for row in range(0, len(board.state)):
            formatted_board += '\n'
            formatted_board += self.add_row_number(row, len(board.state))
            for column in range(0, len(board.state[row])):
                formatted_board += self.add_shot_marker(board, row, column)
        formatted_board += '\n'
        return formatted_board
  
    

