clients = {}

n = int(input("Enter the number of clients\n"))

for i in range(1, n+1):
    print(f"Enter the details of the client {i}")
    name = input().strip()
    email = input().strip()
    passport = input().strip()
    clients[passport] = (name, email, passport)

search_passport = input("Enter the passport number of the client to be searched\n").strip()

if search_passport in clients:
    client = clients[search_passport]
    print("Client Details")
    print(f"{client[0]}--{client[1]}--{client[2]}")
else:
    print("Client not found")