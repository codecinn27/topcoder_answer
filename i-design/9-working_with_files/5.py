# Open the file for reading
with open("SalariesDataSet.csv", "r") as file:
    lines = file.readlines()

# Replace commas with semicolons and print each line
for line in lines:
    print(line.strip().replace(",", ";"))
