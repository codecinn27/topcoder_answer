'''
input: 5
output: 2 3 5 7 11

input :10
output: 2 3 5 7 11 13 17 19 23 29

'''

prime_count = int(input(""))
x = 0
first_prime = 2
while x != prime_count:
    if x ==0:
        print(first_prime,end = " ")
        first_prime +=1
        x+=1
    else:
        not_prime = True
        while not_prime:  
            for y in range(2,first_prime):
                if first_prime%y == 0:
                    first_prime += 1
                    break
            else:
                not_prime = False 
            
        print(first_prime, end=" ")
        first_prime +=1
        x+=1  