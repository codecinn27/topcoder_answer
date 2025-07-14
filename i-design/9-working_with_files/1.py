import re

def calculate_average_word_length():
    try:
        with open('averageLength.txt', 'r') as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text)
            if not words:
                print(0)
                return
            total_length = sum(len(word) for word in words)
            average = total_length / len(words)
            print(int(round(average)))
    except FileNotFoundError:
        print("File 'averageLength.txt' not found.")

calculate_average_word_length()