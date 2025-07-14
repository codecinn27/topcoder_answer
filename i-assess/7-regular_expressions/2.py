import re

# Input
text = input()
shift = int(input())

# Check for overflow first
if any(ord(char) + shift > 127 for char in text):
    print("invalid")
else:
    # Use re.sub with lambda to shift each character
    result = re.sub(r'.', lambda c: chr(ord(c.group(0)) + shift), text)
    print(result)
