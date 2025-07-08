
name = input()
name_output = ""
lenght = len(name)
half = lenght//2

#copy the first half
for i in range(half+(lenght%2)):
    name_output += name[i]

# mirror the second half (excluding middle if odd)
for j in range(half-1, -1, -1):
    name_output += name[j]

print(name_output)

# name = input()
# name_output = ""
# half = len(name)//2
# print(half)
# starting_last = half-1
# print("starting last: ", starting_last)
# if half%2 != 0:
#     half-=1
# for x in range(len(name)):
#     if x>half:
#         name_output+=name[starting_last]
#         starting_last-=1
#     else:
#         name_output+=name[x]

# print(name_output)

# #will fail test -> tese
