n = int(input())
basket = []

for _ in range(n):
    ball = int(input())
    basket.append(ball)

search_ball = int(input())

if search_ball in basket:
    print("Got It!")
else:
    print("Sorry!")