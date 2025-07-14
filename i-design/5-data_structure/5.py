n = int(input())
students = []
for _ in range(n):
    students.append(int(input()))
price_per_book = int(input())

total_books = sum(students)
total_cost = total_books * price_per_book

print(f"Total number of books required : {total_books}")
print(f"Total cost: {total_cost}")