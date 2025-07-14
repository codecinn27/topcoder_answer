import re

# Input
number = input()

# Regex pattern to match valid format: +91- followed by 10 digits
pattern = r'^\+91-\d{10}$'

# Check using regex
if re.match(pattern, number):
    print("Not a Spam Call")
else:
    print("Spam Call")
   