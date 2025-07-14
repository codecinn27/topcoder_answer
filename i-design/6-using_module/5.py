def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("Enter the two positive numbers")
num1 = int(input())
num2 = int(input())

result = gcd(num1, num2)
print(f"GCD:{result}")