n = int(input("Enter total Number of sheets: \n"))
sheets = []
for _ in range(n):
    reg_nums = tuple(map(int, input().split()))
    sheets.append(reg_nums)

print(f"Attendance Sheets with Register Number: {tuple(sheets)}")

unique_reg_nums = sorted(set(num for sheet in sheets for num in sheet))
print(f"Final sheet: {tuple(unique_reg_nums)}")