ROWS = {
        '1': 0,
        '2': 1,
        '3': 2,
        '4': 3,
        '5': 4,
        '6': 5,
        '7': 6,
        '8': 7,
        '9': 8,
        '10': 9,
        }

COLUMNS = {
           'A': 0,
           'B': 1,
           'C': 2,
           'D': 3,
           'E': 4,
           'F': 5,
           'G': 6,
           'H': 7,
           'I': 8,
           'J': 9,
           }

COL_LETS = [chr(i) for i in range(ord('A'), ord('J')+1)]
ROW_NUMS = [str(i) for i in range(1, 11)]
ALL_SPOTS = [(let + num) for let in COL_LETS for num in ROW_NUMS]
