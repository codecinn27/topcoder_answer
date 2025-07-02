registration_code = input()

if int(registration_code) < 10:
    print("Invalid Input")
else:
    num = int(registration_code)%10 - int(registration_code[0])
    print(abs(num))