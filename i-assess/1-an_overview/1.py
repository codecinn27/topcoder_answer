total_people = 0
total = 0

for x in range(3):
    a= float(input(f"Enter the number of people who watched show {x+1} "))
    b = float(input(f"Enter the average rating for show {x+1} "))
    total_people += a
    total += a*b

answer = round(total/total_people,2)
print(f"The overall average rating for the show is {answer:.2f}")