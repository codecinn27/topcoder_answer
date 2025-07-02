characters = []
numbers = []

for _ in range(3):
    c, n = input().split()
    characters.append(c)
    numbers.append(n)

if len(set(characters)) == 1 and len(set(numbers)) == 1:
    print("Double Bonanza")
elif len(set(characters)) == 1 or len(set(numbers)) == 1:
    print("Bonanza")
else:
    print("No Bonanza")