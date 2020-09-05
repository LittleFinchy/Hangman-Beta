from letter import Letter

class Word:

    def __init__(self, input_text):
        self.input_text = input_text
        self.input_text_letters = []
        for char in self.input_text:
            self.input_text_letters.append(Letter(char))
    
    def show(self):
        temp_word = []
        for char in self.input_text_letters:
            if char.found:
                temp_word.append(char.letter)
            else:
                temp_word.append('_')
        print(''.join(temp_word))