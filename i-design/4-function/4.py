cal_string = '''
Select the operation
1.Add
2.Subtract
3.Multiply
4.Divide
5.Modulus
Enter the choice(1/2/3/4/5):
'''

def addition(n1,n2):
    temp = n1+n2
    print(f"{n1} + {n2} = {temp}")

def subtraction(n1,n2):
    temp = n1-n2
    print(f"{n1} - {n2} = {temp}")

def multiplication(n1,n2):
    temp = n1*n2
    print(f"{n1} * {n2} = {temp}")

def division(n1,n2):
    temp = n1/n2
    print(f"{n1} / {n2} = {temp}")

def modulus(n1,n2):
    temp = n1%n2
    print(f"{n1} % {n2} = {temp}")

def calculator():
    decision = int(input(cal_string))
    #decision = int(input())
    if decision>5:
        print("Invalid Input")
    else:
        first_val = int(input("Enter the first number\n"))
        second_val = int(input("Enter the second number\n"))
        #first_val = int(input())
        #second_val = int(input())
        if decision == 1:
            addition(first_val,second_val)
        elif decision == 2:
            subtraction(first_val, second_val)
        elif decision == 3:
            multiplication(first_val, second_val)
        elif decision == 4:
            division(first_val, second_val)
        else:
            modulus(first_val,second_val)

calculator()