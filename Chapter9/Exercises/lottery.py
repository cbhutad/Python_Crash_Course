from random import choice

class Lottery:

    def __init__(self):
        self.symbols = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E')

    def show_winning_combo(self):
        combo = []
        for i in range(4):
            combo.append(choice(self.symbols))
        print(f"Winning combo : {combo}")