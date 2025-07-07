try:
    n = int(input("Enter size of list\n"))
    if n <= 0:
        print("Invalid input")
    else:
        print("Enter the elements in list")
        val_list = []
        for _ in range(n):
            val = int(input())
            val_list.append(val)

        # Filter using lambda function
        divisible_by_13 = list(filter(lambda x: x % 13 == 0, val_list))

        # Print the result
        for num in divisible_by_13:
            print(num, end=" ")

except ValueError:
    print("Invalid input")
