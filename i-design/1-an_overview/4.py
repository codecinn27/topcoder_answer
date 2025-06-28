x = int(input("Enter the value of X"))
y = int(input("Enter the value of Y"))

children = int((y-5*x)/13)
adult = int(x + children)
senior = int(2*children)
print(f"Number of children tickets sold : {children}")
print(f"Number of adult tickets sold : {adult}")
print(f"Number of senior tickets sold : {senior}")
print("Number of senior tickets sold : ")

'''
explanation:

adult = x + children
senior = 2 * children
y = adult + senior + children
y = 5(x+children) + 3(2*children) + 2children
y = 5x + 5children + 6children + 2children
y-5x = 13 children
children = int((y-5x)/13)



'''