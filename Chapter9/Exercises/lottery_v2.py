from random import choice

class Lottery:

    def __init__(self):
        self.symbols = (1, 2, 3)

    def show_winning_combo(self):
        combo = []
        for i in range(3):
            combo.append(choice(self.symbols))
        return combo

    def you_rolled(self):
        userroll = []
        for i in range(3):
            userroll.append(choice(self.symbols))
        return userroll
        