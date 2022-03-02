import random

STARTER_POSSIBLE_ANSWERS = "word lists/wordle_possible_answers.txt"
REMAINING_POSSIBLE_ANSWERS = "word lists/remaining_possible_answers.txt"


class DataManipulator:
    def __init__(self):
        self.open_and_write_orginal_file(STARTER_POSSIBLE_ANSWERS)

    # Init methods
    def open_and_write_orginal_file(self, filename):
        with open(filename, "r") as pa:
            with open(REMAINING_POSSIBLE_ANSWERS, "w") as rpa:
                for line in pa:
                    rpa.write(line)

    def write_with_removed_words(self, letter_to_remove: str):
        """Removes words from remaining_possible_answers based on letter provided

        Args:
            letter_to_remove ("character"):
            The letter that is provided will be
            removed from all words in the document
        """
        with open(REMAINING_POSSIBLE_ANSWERS, "r") as read_file:
            lines = read_file.readlines()
            with open(REMAINING_POSSIBLE_ANSWERS, "w") as write_file:
                remaining_answers = self.remove_words_from_list_with_letter(
                    lines,
                    letter_to_remove.lower()
                    )
                for line in remaining_answers:
                    write_file.write(line)

    # Use methods
    def remove_words_from_list_with_letter(
        self,
        list_of_words: list[str],
        letter: str
    ):
        return [word for word in list_of_words if letter not in word]

    # Fix this
    def return_random_line(self):
        lines = open(REMAINING_POSSIBLE_ANSWERS).read().splitlines()
        myline = random.choice(lines)
        return myline

    def is_letter_in_word(self, letter: str, word: str):
        return letter.lower() in word

    def remove_lines_with_words_in_index(
        self,
        list_of_words: list[str],
        letter: str,
        index: int
    ):
        return [word for word in list_of_words if word[index] != letter]

    def remove_lines_with_letters_not_in_index(
        self,
        list_of_words: list[str],
        letter: str,
        index: int
    ):
        return [word for word in list_of_words if word[index] == letter]


if __name__ == "__main__":
    dm = DataManipulator()
    while True:
        letter = input("Letter: ")
        dm.write_with_removed_words(letter)
        print(dm.return_random_line())
