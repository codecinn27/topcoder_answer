'''
1) square square then floor to find the largest square value for the tile 
2) get the largest square value for tile then multiply by the square tile to get the final output 


import math

side = int(input("Enter the side in cm of a square tile"))
available = int(input("Enter the number of square tiles available"))

square_val =  math.isqrt(available)
max_val = (side**2)*(square_val**2)

print("square value ", square_val)
print("max value ", max_val)

print(f"Area of the largest possible square is {max_val}sqcm")

'''

side = int(input("Enter the side in cm of a square tile"))
available = int(input("Enter the number of square tiles available"))


square_val =  int(available**0.5)
max_val = (side**2)*(square_val**2)
print(f"Area of the largest possible square is {max_val}sqcm")