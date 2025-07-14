import re

input_str = input().strip()
numbers = re.findall(r'\d+', input_str)

if numbers:
    max_number = max(map(int, numbers))
    print(max_number)
else:
    print("No Password")