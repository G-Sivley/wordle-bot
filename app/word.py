from letter import Letter


class Word:
    def __init__(self, word: str, list_of_word_states):
        self.word = word
        self.list_of_word_states = list_of_word_states
        self.letters = []

    def create_letters(self):
        new_list = []
        for idx, letter in enumerate(self.word):
            new_list.append(Letter(letter, self.list_of_word_states[idx], idx))
        return new_list
