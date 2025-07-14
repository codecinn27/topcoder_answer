n = int(input())
students = {}

for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(int, data[1:]))
    students[name] = marks

search_name = input().strip()

if search_name not in students:
    print("Student doesn't exist")
else:
    marks = students[search_name]
    unique_marks = sorted(set(marks), reverse=True)
    
    if len(unique_marks) == 1:
        print(f"{search_name} scored same marks in all subjects: {unique_marks[0]}")
    else:
        print(f"Second Highest mark of {search_name}: {unique_marks[1]}")