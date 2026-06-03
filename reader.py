def read_text_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: '{filepath}' was not found."
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    path = input("Enter the path to the text file: ")
    print("\n--- File Contents ---\n")
    print(read_text_file(path))