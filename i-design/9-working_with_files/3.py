def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        print(f"The file has {line_count} lines")
    except FileNotFoundError:
        print(f"File {filename} not found.")

# Example usage:
count_lines_in_file('input.txt')