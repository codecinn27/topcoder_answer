n = int(input())

if n == 0:
    print("")
elif n == 1:
    print("0")
else:
    fib_series = [0, 1]
    for i in range(2, n):
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    print(' '.join(map(str, fib_series)))   