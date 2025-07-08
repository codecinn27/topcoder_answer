name = input()
half = len(name) // 2

# If even length
if len(name) % 2 == 0:
    first_half = name[:half]
    name_output = first_half + first_half[::-1]
else:
    first_half = name[:half + 1]
    name_output = first_half + first_half[:-1][::-1]

print(name_output)
