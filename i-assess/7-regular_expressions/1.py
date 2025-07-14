import re

# Input
text = input()

# Regex to match names with initials and surnames
pattern = r'(?:[A-Z]\.)?[A-Z][a-z]+(?:\s[A-Z][a-z]+)*'

# Find all matches
matches = re.findall(pattern, text)

# Print each name on a new line
for name in matches:
    print(name)
