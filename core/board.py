class Board:
    def __init__(self):
        self.state = [[None for ele in range(10)] for index in range(10)]

    def format(self):
        formatted_board = '\n' + '    A  B  C  D  E  F  G  H  I  J'

        for row in range(0, len(self.state)):
            formatted_board += '\n'
            if (row + 1) < 10:
                formatted_board += ' ' + str(row + 1) + ' '
            else:
                formatted_board += str(row + 1) + ' '
            for column in range(0, len(self.state[row])):
                if self.state[column][row] is None:
                    formatted_board += '[ ]'
                else:
                    formatted_board += '[X]'

        formatted_board += '\n'
        return formatted_board

    def update(self, user_shot_choice):
        letters = {
                'A': 0,
                'B': 1,
                'C': 2,
                'D': 3,
                'E': 4,
                'F': 5,
                'G': 6,
                'H': 7,
                'I': 8,
                'J': 9
                }
        numbers = {
                '1': 0,
                '2': 1,
                '3': 2,
                '4': 3,
                '5': 4,
                '6': 5,
                '7': 6,
                '8': 7,
                '9': 8,
                '10': 9
                }
        user_letter = user_shot_choice[0]
        user_num = user_shot_choice[1:]

        self.state[letters[user_letter]][numbers[user_num]] = 'X'
