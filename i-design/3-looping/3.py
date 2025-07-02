'''
input: 5
output: 30 35 38 41 54

input :10
output: 30 35 38 41 54 53 78 71 110 95

'''

odd_starting = 30
even_starting = 35

adding_odd = 8
adding_even = 6

count = int(input(""))
for x in range(count):
    if x%2 == 0:
        print(odd_starting, end=" ")
        odd_starting += adding_odd
        adding_odd += 8
    else:
        print(even_starting, end=" ")
        even_starting += adding_even
        adding_even += 6
        