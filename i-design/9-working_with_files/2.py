def sum_integers_in_file(filename):
    total = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    num = int(line.strip())
                    total += num
                except ValueError:
                    # Skip lines that cannot be converted to integers
                    continue
        print(f"The sum of the integers in the file {filename} is:{total}")
    except FileNotFoundError:
        print(f"File {filename} not found.")

# Example usage:
sum_integers_in_file('sample.txt')