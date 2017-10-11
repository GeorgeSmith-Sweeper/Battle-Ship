class Game:
    def __init__(self, board, ui, validate):
        self.ui = ui
        self.board = board
        self.validate = validate

    def play(self): 
        self.ui.display("Welcome to Battleship")
        board_full = False
        while not board_full:
            board_full = self.validate.board_full(self.board.state)
            self.ui.display("Take your best shot")
            self.ui.display(self.board.format())
            spot_choice = self.validate.spot_occupied(self.board.state, self.ui)
            self.board.update(spot_choice)

class TerminalUi:
    def display(self, message):
       print(message)

    def get_input(self, prompt_string):
        response = input(prompt_string)
        return response

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

class Validate:
    def __init__(self):
        self.letters = [chr(i) for i in range(ord('A'), ord('J')+1)]
        self.numbers = [str(i) for i in range(1, 11)]
        self.all_spots = [(let + num) for let in self.letters for num in self.numbers]
    
    def board_full(self, board_state):
        full = True
        for row in range(0, len(board_state)):
            for ele in board_state[row]:
                if ele is None:
                    full = False
        return full

    def spot_exists(self, ui):
        user_shot_choice = ui.get_input('>>')
        while user_shot_choice not in self.all_spots:
            ui.display('Spot does not exist, Try again')
            user_shot_choice = ui.get_input('>>')
        return user_shot_choice

    def spot_occupied(self, board_state, ui):
        user_shot_choice = self.spot_exists(ui)
        lets = {
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
        nums = {
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
        while board_state[lets[user_letter]][nums[user_num]] is not None:
            ui.display('That spot is occupied. Pick a different spot')
            user_shot_choice = ui.get_input('>>')
            user_letter = user_shot_choice[0]
            user_num = user_shot_choice[1:]
        return user_shot_choice

if __name__ == "__main__":
    board = Board()
    ui = TerminalUi()
    validate = Validate()
    game = Game(board, ui, validate)
    game.play()
