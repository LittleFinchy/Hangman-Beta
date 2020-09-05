class Letter:

    def __init__(self, letter, found=False):
        self.letter = letter
        self.found = found

    def show(self):
        print(self.letter)