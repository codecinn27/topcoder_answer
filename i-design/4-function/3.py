def GCD(n1, n2):
    if n1 == 0:
        return abs(n2) #GCD(0, 0) is undefined (some define it as 0, but it's usually avoided)
    if n2 == 0:
        return abs(n1)

    temp = 1
    for x in range(1, min(n1, n2) + 1):  # changed from 2 → 1, GCD(0,5) , GCD(7,13)
        if n1 % x == 0 and n2 % x == 0:
            temp = x
    return temp
'''
GCD(0,5) return 5
GCD(7,13) return 1
'''

def LCM(n1, n2):
    return abs(n1 * n2) // GCD(n1, n2)  # added abs() for safety

def print_output(n1, n2):
    gcd = GCD(n1, n2)
    lcm = LCM(n1, n2)
    print(f"Greatest common divisor of {n1} and {n2} = {gcd}")
    print(f"Least common multiple of {n1} and {n2} = {lcm}")

print("Enter two integers:")
value1 = int(input())
value2 = int(input())
print_output(value1, value2)
