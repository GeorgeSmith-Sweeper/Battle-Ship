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
                    return False
        return full

    def spot_exists(self, ui):
        user_shot_choice = ui.get_input('>>')

        while user_shot_choice not in self.all_spots:
            ui.display('Spot does not exist, Try again')
            user_shot_choice = ui.get_input('>>')
        return user_shot_choice

    def spot_occupied(self, board_state, ui):
        user_shot_choice = self.spot_exists(ui)
        user_letter = user_shot_choice[0]
        user_num = user_shot_choice[1:]
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

        while board_state[lets[user_letter]][nums[user_num]] is not None:
            ui.display('That spot is occupied. Pick a different spot')
            print(user_letter, user_num)
            user_shot_choice = self.spot_exists(ui)
            user_letter = user_shot_choice[0]
            user_num = user_shot_choice[1:]
        return user_shot_choice
