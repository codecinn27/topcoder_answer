# Input: two strings
word1 = input()
word2 = input()

# Reverse the second word for easier access
word2_reversed = word2[::-1]

# Get the lengths
len1 = len(word1)
len2 = len(word2)

# Encrypted result list
encrypted = []

# Get the max length of both words
max_len = max(len1, len2)

# Build the encrypted string
for i in range(max_len):
    if i < len1:
        encrypted.append(word1[i])
    if i < len2:
        encrypted.append(word2_reversed[i])

# Output the result
print("".join(encrypted))
