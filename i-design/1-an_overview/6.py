total_sal = int(input("Enter the total salary paid"))

'''
weekday = weekend + 10
80 * weekday 
50 * weekend 
total_sal = weekday(total hour rate) + weekend(total hour rate)
total_sal = 80 * (weekend +10) + 50 * weekend
total_sal = 80weekend + 800 + 50 weekend
total_sal - 800 = 130weekend
(total_sal-800)/130 = weekend
'''

weekend = int((total_sal-800)/130)
weekday = int(weekend + 10)
print(f"Number of weekday hours is {weekday}")
print(f"Number of weekend hours is {weekend}")