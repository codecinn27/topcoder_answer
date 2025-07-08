name = input()
name_output = ""
half = int(len(name)/2)
starting_last = half-1
for x in range(len(name)):
    if x>half:
        name_output+=name[starting_last]
        starting_last-=1
    else:
        name_output+=name[x]

print(name_output)
