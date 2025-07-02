def GCD(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

def LCM(n1, n2):
    return (n1 * n2) // GCD(n1, n2)

def print_output(n1, n2):
    gcd = GCD(n1, n2)
    lcm = LCM(n1, n2)
    print(f"Greatest common divisor of {n1} and {n2} = {gcd}")
    print(f"Least common multiple of {n1} and {n2} = {lcm}")

print("Enter two integers:")
value1 = int(input())
value2 = int(input())
print_output(value1, value2)
