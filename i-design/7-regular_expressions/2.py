# Input
s = input()

# Define set of required vowels
vowels = {'a', 'e', 'i', 'o', 'u'}

# Get all vowels found in the string
found = set(c for c in s if c in vowels)

# Check if all vowels are present
if vowels.issubset(found):
    print("Accepted")
else:
    print("Not Accepted")
