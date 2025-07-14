def reverse_words_in_file():
    try:
        with open('input.txt', 'r') as input_file:
            content = input_file.read()
            words = content.split()
            reversed_words = ' '.join(reversed(words))
        with open('output.txt', 'w') as output_file:
            output_file.write(reversed_words)
    except FileNotFoundError:
        print("File 'input.txt' not found.")

reverse_words_in_file()