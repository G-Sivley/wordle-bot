from data_manipulator import DataManipulator


def app():
    dm = DataManipulator()

    print("type: 'quit' to exit")
    while True:
        letter = input("Gray letters: ")
        if letter == "quit":
            break

        dm.write_with_removed_words(letter)

if __name__ == "__main__":
    app()
