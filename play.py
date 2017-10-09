class Game:
    def __init__(self, board, ui):
        self.ui = ui
        self.board = board

    def play(self):
        self.ui.display("Welcome to Battleship")
        self.ui.display("Take your best shot")
        self.ui.display(self.board.format())
        valid_spot = ValueError
        while valid_spot == ValueError:
            valid_spot =  self.board.validate(self.ui.get_input('>>'))
        self.board.update(valid_spot)
        self.ui.display(self.board.format())

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
        formatted_board = ''
        for row in range(0, len(self.state)):
            formatted_board += '\n'
            for column in range(0, len(self.state[row])):
                if self.state[column][row] is None:
                    formatted_board += '[ ]'
                else: 
                    formatted_board += '[X]'
        formatted_board += '\n'
        return formatted_board
    
    def validate(self, user_shot_choice):
        letters = [chr(i) for i in range(ord('A'), ord('J')+1)]
        numbers = list(range(1, 11))

        for x in range(0, len(numbers)):
            numbers[x] = str(numbers[x])
            
        all_spots = []
        for let in range(0, len(letters)):
            for num in numbers:
                all_spots.append(letters[let] + num)
        
        if user_shot_choice in all_spots:
            return user_shot_choice
        return ValueError

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

if __name__ == "__main__":
    board = Board()
    ui = TerminalUi()
    game = Game(board, ui)
    game.play()
