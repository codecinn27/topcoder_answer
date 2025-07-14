# Read input
message = input().strip()
split_char = input().strip()

# Split the message and capitalize first letters
split_words = [word.capitalize() for word in message.split(split_char)]

# Print output
print("Strings after splitting")
for word in split_words:
    print(word)