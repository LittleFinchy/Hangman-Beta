import random

class Word:
    pass

class Game(Word):
    def __init__(self,level,hints,health):
        self.level = level
        self.hints = hints
        self.health = health
        self.word = Word(self.level)


