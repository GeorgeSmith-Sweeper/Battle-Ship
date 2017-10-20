class TerminalUi:
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
    
    def add_shot_marker(self, board_state, row, column, ship_symbols):
        if board_state[row][column] is None or board_state[row][column] in ship_symbols:
            return '[ ]'
        if board_state[row][column] == 'Miss': 
            return '[M]'
        elif board_state[row][column] == 'Hit':
            return '[H]'
    
    def format(self, board_state, all_ships):
        ship_symbols = []
        for ship in all_ships:
            ship_symbols.append(ship['symbol'])

        formatted_board = '\n' + '    A  B  C  D  E  F  G  H  I  J'
        
        for row in range(0, len(board_state)):
            formatted_board += '\n'
            formatted_board += self.add_row_number(row, len(board_state))
            for column in range(0, len(board_state[row])):
                formatted_board += self.add_shot_marker(board_state, row, column, ship_symbols)
        formatted_board += '\n'
        return formatted_board
  
    
