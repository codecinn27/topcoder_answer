def isPrime(n):
    if n<2:
        return False
    elif n==2:
        return True
    elif n%2 == 0:
        return False
    for x in range(3, int(n**0.5)+1,2):
        if n%x == 0:
            return False
    return True

start_val = int(input())
final_val = int(input())

for x in range(start_val, final_val+1):
    if isPrime(x):
        print(x, end=" ")