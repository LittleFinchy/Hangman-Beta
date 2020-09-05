class Game:

    def __init__(self, number_of_guesses=10):
        self.number_of_guesses = number_of_guesses
        self.past_guesses = []

    def use_guess(self):
        self.number_of_guesses -= 1

    def show_past_guesses(self):
        print(''.join(self.past_guesses))