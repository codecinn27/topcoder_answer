from collections import OrderedDict

def first_non_repeating_char(input_str):
    char_count = OrderedDict()
    
    # Count occurrences of each character
    for char in input_str:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the first character with count 1
    for char, count in char_count.items():
        if count == 1:
            return char
    
    return '#'

# Read input
input_string = input().strip()

# Get and print result
result = first_non_repeating_char(input_string)
print(result)