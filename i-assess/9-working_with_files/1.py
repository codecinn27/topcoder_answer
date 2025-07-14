from collections import Counter

# Step 1: Read the content of the input file
with open("frequencyFile.txt", "r") as file:
    text = file.read().lower()  # convert to lowercase for case-insensitive counting

# Step 2: Filter only alphabetic characters
filtered_letters = [char for char in text if char.isalpha()]

# Step 3: Count frequencies using Counter
letter_counts = Counter(filtered_letters)

# Step 4: Print sorted output
for letter in sorted(letter_counts):
    print(f"{letter}: {letter_counts[letter]}")
