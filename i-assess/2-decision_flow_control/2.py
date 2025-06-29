same_type = True
same_val = True

previous_type, previous_val = input().split()
previous_val = int(previous_val)
for x in range(2):
    card_type, card_val = input().split()
    card_val = int(card_val)
    if previous_type != card_type:
        same_type = False
    if previous_val != card_val:
        same_val = False

if same_type and same_val:
    print("Double Bonanza")
elif same_type or same_val:
    print("Bonanza")
else:
    print("No Bonanza")
    