def read_file(file_path):
    """Attempt to open and read a file, handling FileNotFoundError if the file does not exist."""
    try:
        with open(file_path, 'r') as file:
            # Read the contents of the file
            content = file.read()
            return content
    except FileNotFoundError:
        # Handle the case where the file is not found
        return "Error: The file was not found."

if __name__ == "__main__":
    # Specify the path to the file
    file_path = input("Enter the path to the file: ")
    # Read and print the file content or error message
    print(read_file(file_path))
