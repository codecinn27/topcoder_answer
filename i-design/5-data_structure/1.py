name = input()
val = int(input())

if val-1 < len(name):
    name = name[:val -1] + name[val:]

print(name)