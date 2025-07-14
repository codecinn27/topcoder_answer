# Read the number of persons
n = int(input())

# Open the output file in write mode
with open("salaryData.csv", "w") as outfile:
    # Loop to read name and salary for each person
    for _ in range(n):
        name = input().strip()
        salary = input().strip()
        # Write to the file in the format: name,salary
        outfile.write(f"{name},{salary}\n")
