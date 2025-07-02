def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):  # check only odd numbers up to sqrt(n)
        if n % i == 0:
            return False
    return True

prime_count = int(input())
count = 0
num = 2

while count < prime_count:
    if is_prime(num):
        print(num, end=" ")
        count += 1
    num += 1
