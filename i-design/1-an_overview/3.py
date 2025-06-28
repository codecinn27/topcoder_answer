b_exp = int(input("Enter branding expenses"))
trav_exp = int(input("Enter travel expenses"))
food_exp = int(input("Enter food expenses"))
logis_exp = int(input("Enter logistics expenses"))
total = b_exp + trav_exp + food_exp + logis_exp
b_per = (b_exp/total) * 100
trav_per = (trav_exp/total) * 100
food_per = (food_exp/total) * 100
logis_per = (logis_exp/total) * 100
print(f"Total expenses: Rs.{total:.2f}")
print(f"Branding expenses percentage : {b_per:.2f}%")
print(f"Travel expenses percentage : {trav_per:.2f}%")
print(f"Food expenses percentage : {food_per:.2f}%")
print(f"Logistics expenses percentage : {logis_per:.2f}%")