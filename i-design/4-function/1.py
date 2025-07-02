def greet(x, y = "Welcome to Python Programming"):
    print(f"Hello {x}, {y}")


def input_menu():
    print("Menu")   
    print("1. Name and Message")   
    print("2. Name")
    temp = int(input())   
    name = input("Enter the name")
    if temp == 1:
        message = input("Enter the message")
        greet(name, message)
    else:
        greet(name)


input_menu()

