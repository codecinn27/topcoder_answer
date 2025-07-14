try:
    matches = int(input("Enter the number of matches\n"))
    if matches <= 0:
        print("Number of matches must be positive")
    else:
        total = 0
        print("Enter the scores")
        for _ in range(matches):
            try:
                score = int(input())
                total += score
            except ValueError:
                print("Type Error Exception")
                exit()
        average = total / matches
        print(f"Batting average: {average:.2f}")
except ValueError:
    print("Type Error Exception")