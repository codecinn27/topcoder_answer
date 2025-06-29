num = int(input(""))
last_digit = num % 10
if last_digit == 3 or last_digit == 8:
    print("Lucky Winner")
else:
    print("Not a Lucky Winner")