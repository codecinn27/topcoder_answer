input_count = int(input(""))
list_val = []
even_count = 0
odd_count = 0
for x in range(input_count):
    temp = int(input(""))
    list_val.append(temp)
    if temp%2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count, end=" ")
print(odd_count, end=" ")
