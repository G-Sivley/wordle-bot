from data_manipulator import DataManipulator
from letter import Letter


def app():
    dm = DataManipulator()

    print("type: 'quit' to exit")
    while True:

        print(dm.return_random_line())
        letter = input("Letters: ")
        if letter == "quit":
            break

        color = input("Color (r, y, g): ")

        index = int(input("Index: "))

        letter = Letter(letter, color, index)
        dm.write_with_removed_words(letter)


if __name__ == "__main__":
    app()
