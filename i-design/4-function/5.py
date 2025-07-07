n = int(input("Enter size of list\n"))
# fill your code here
val_list = []
divisible_list = []
for x in range(n):
    temp = abs(int(input("Enter the elements in list")))
    val_list.append(temp)
    if temp%13 == 0:
        divisible_list.append(temp)

for x in divisible_list:
    print(x, end=" ")


