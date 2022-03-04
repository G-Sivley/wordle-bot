from letter import Letter

class WordHandler:
    def __init__(self):
        self.guess_str = None
        self.colors = None
        self.word = []
    
    def get_guess_str(self):
        return input("Type in word: ").lower()
    
    def get_colors(self):
        return input("Add colors in order (r: no match, y: not right position, g: right position\n").lower()
    
    def request_input(self):
        self.get_guess_str()
        self.get_colors()
        self.make_word()
    
    def make_word(self):
        for idx, character in enumerate(self.guess_str):
            color = self.colors[idx]
            letter = Letter(character, color, idx)
            self.word.append(letter)
       