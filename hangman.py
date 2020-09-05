from word import Word
from guess import Guess
from game import Game

temp_game = Game()

temp_answer = 'banana bread'

hidden_word = Word(temp_answer)

while temp_game.number_of_guesses > 0:
    my_guess = Guess(input('Guess: '))
    my_guess.check_guess(hidden_word, temp_game)
    print('Guess '+str(temp_game.number_of_guesses))