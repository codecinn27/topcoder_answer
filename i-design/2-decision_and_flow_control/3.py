price = int(input(""))
ticket_num = int(input(""))
if ticket_num > 500:
    total = price * ticket_num * 0.5
elif ticket_num > 400:
    total = price * ticket_num * 0.6
elif ticket_num > 200:
    total = price * ticket_num * 0.7
elif ticket_num > 100:
    total = price * ticket_num *0.8
elif ticket_num > 49:
    total = price * ticket_num *0.9
else:
    total = price * ticket_num

print(f"{total:.2f}")
