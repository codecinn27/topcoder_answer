import re

# Input
pan = input()

# Regex pattern for valid PAN
pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'

# Check match
if re.match(pattern, pan):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")
