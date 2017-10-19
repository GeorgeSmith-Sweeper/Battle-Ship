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
                if board_state[column][row] is None or board_state[column][row] in ship_symbols:
                    formatted_board += '[ ]'
                else:
                    formatted_board += '[X]'

        formatted_board += '\n'
        return formatted_board
    
