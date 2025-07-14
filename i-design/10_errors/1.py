try:
    num1 = int(input("Enter number 1\n"))
    num2 = int(input("Enter number 2\n"))
    
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Divide By Zero Error")
