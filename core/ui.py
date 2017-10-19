class TerminalUi:
    def display(self, message):
       print(message)

    def get_input(self, prompt_string):
        response = input(prompt_string)
        return response

    def format(self, board_state, all_ships):
        ship_symbols = []
        for ship in all_ships:
            ship_symbols.append(ship['symbol'])

        formatted_board = '\n' + '    A  B  C  D  E  F  G  H  I  J'
        
        for row in range(0, len(board_state)):
            formatted_board += '\n'
            if (row + 1) < 10:
                formatted_board += ' ' + str(row + 1) + ' '
            else:
                formatted_board += str(row + 1) + ' '

            for column in range(0, len(board_state[row])):
                if board_state[row][column] is None or board_state[row][column] in ship_symbols:
                    formatted_board += '[ ]'

                if board_state[row][column] == 'Miss': 
                    formatted_board += '[M]'
                elif board_state[row][column] == 'Hit':
                    formatted_board += '[H]'

        formatted_board += '\n'
        return formatted_board
    
