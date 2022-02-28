STARTER_POSSIBLE_ANSWERS = "word lists/wordle_possible_answers.txt"
REMAINING_POSSIBLE_ANSWERS = "word lists/remaining_possible_answers.txt"


class DataManipulator:
    def __init__(self):

        self.open_and_read_file(STARTER_POSSIBLE_ANSWERS)
    
    ### Init methods
    
    def open_and_read_file(self, filename):
        with open(filename, "r") as pa:
            self.write_remaining_possible_answers(starter_file=pa, filename=REMAINING_POSSIBLE_ANSWERS)
             
    def write_remaining_possible_answers(self, starter_file, filename):
        with open(filename, "w") as rpa:
            for line in starter_file:
                rpa.write(line)
        

    ### Use methods
    
    def remove_excluded_answers(self):
        pass

    def is_letter_in_word(self, letter: str, word: str):
        return letter.lower() in word

if __name__ == "__main__":
    dm = DataManipulator()