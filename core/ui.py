import helpers.constants as consts


class TerminalUi:

    def __init__(self):
        self.COMP_WIN_MSG = consts.COMP_WIN_MSG
        self.HUMAN_WIN_MSG = consts.HUMAN_WIN_MSG
        self.WELCOME_MSG = consts.WELCOME_MSG
        self.INSTRUCTIONS = consts.INSTRUCTIONS
        self.HIT_MARKER = consts.HIT_MARKER
        self.MISS_MARKER = consts.MISS_MARKER
        self.SUNK_MARKER = consts.SUNK_MARKER
        self.BLANK_SPACE = consts.BLANK_SPACE

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

    def spot_value(self, board, row, column):
        return board.state[row][column]

    def is_space_blank(self, spot_value, board):
        return spot_value is None or spot_value in board.all_ships

    def is_space_miss(self, spot_value):
        return spot_value == consts.MISS

    def is_space_hit(self, spot_value):
        return spot_value == consts.HIT

    def is_space_sunk(self, spot_value):
        return spot_value == consts.SUNK

    def add_shot_marker(self, board, row, column):
        spot_value = self.spot_value(board, row, column)
        if self.is_space_blank(spot_value, board):
            return self.BLANK_SPACE
        if self.is_space_miss(spot_value):
            return self.MISS_MARKER
        if self.is_space_hit(spot_value):
            return self.HIT_MARKER
        if self.is_space_sunk(spot_value):
            return self.SUNK_MARKER

    def terminal_board(self, board):
        formatted_board = '\n' + '    A  B  C  D  E  F  G  H  I  J'

        for row in range(0, len(board.state)):
            formatted_board += '\n'
            formatted_board += self.add_row_number(row, len(board.state))
            for column in range(0, len(board.state[row])):
                formatted_board += self.add_shot_marker(board, row, column)
        formatted_board += '\n'
        return formatted_board
