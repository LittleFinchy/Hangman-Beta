from letter import Letter

class Guess:

    def __init__(self, letter_guess):
        self.letter_guess = Letter(letter_guess)

    def check_guess(self, answer, game):
        found_one = False
        for char in answer.input_text_letters:
            if self.letter_guess.letter == char.letter:
                char.found = True
                found_one = True
        if not found_one:
            game.past_guesses.append(char.letter)
            game.use_guess()
        answer.show()