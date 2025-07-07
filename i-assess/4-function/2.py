def multiVarFunc():
    department = input("Enter department name:")
    student = int(input("Enter the number of total students:"))
    faculties = int(input("Enter the number of total faculties:"))

    return department, student, faculties


department, student, faculties = multiVarFunc()
print("Details:")
print(f"Department:{department}")
print(f"Total students:{student}")
print(f"Total faculties:{faculties}")