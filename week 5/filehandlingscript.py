# file_handling_assignment.py

def create_file():
    try:
        # Create a new text file and write content to it
        with open("my_file.txt", 'w') as file:
            file.write("This is line 1 with some text.\n")
            file.write("The number is 42 on line 2.\n")
            file.write("Line 3: Python is awesome!\n")
        print("File created and written successfully.")
    except Exception as e:
        print(f"Error during file creation: {e}")
    finally:
        print("File creation process finished.")


def read_file():
    try:
        # Read the contents of the file and display them
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("\nContents of 'my_file.txt':\n")
            print(content)
    except FileNotFoundError:
        print("File not found. Please ensure the file exists.")
    except Exception as e:
        print(f"Error while reading the file: {e}")
    finally:
        print("File reading process finished.")


def append_file():
    try:
        # Append additional lines to the file
        with open("my_file.txt", 'a') as file:
            file.write("This is the first appended line.\n")
            file.write("The number 100 is in this appended line.\n")
            file.write("Appended line 3: Learning Python is fun!\n")
        print("Content appended successfully.")
    except Exception as e:
        print(f"Error while appending to the file: {e}")
    finally:
        print("File appending process finished.")


def main():
    # Creating and writing to the file
    create_file()

    # Reading and displaying the contents of the file
    read_file()

    # Appending to the file
    append_file()

    # Reading again to see the updated content
    read_file()


if __name__ == "__main__":
    main()
