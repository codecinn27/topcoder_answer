basic = int(input(""))

if basic < 15000:
    hra = 0.15*basic
    da = 0.9 * basic
else:
    hra = 5000
    da = 0.98 * basic
gross_salary = basic + hra + da
print(f"{gross_salary:.2f}")