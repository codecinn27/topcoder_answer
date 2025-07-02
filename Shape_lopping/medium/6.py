'''
* # # # # # *
# * # # # * #
# # * # * # #
# # # * # # #
# # * # * # # 
# * # # # * #
* # # # # # *

'''
repetition_x = int(input())
first_val = 0
last_val = repetition_x - 1 
for y in range(repetition_x):
    for x in range(repetition_x):
        if x == first_val or x == last_val:
            print("*", end=" ")
        else:
            print("#", end=" ")
    first_val +=1
    last_val -= 1
    print()
