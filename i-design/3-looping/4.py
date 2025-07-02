'''
input : A, B, N
N = number of turns
A = richie starting value 
B = rich starting value
Richie and Riya play a game called "Lucky Pairs".
Richie starts with number A, and Riya starts with number B.
They take turns multiplying their number by 2, for a total of N turns.
Richie always starts first.
After N turns, Richie's number becomes C, and Riya's number becomes D.
The team's final score is the sum: C + D.

Sample Input 1:
1 2 1

Sample Output 1:
4

Sample Input 2:
3 2 3



'''

A, B, N = map(int,input().split())

for x in range(N):
    if x%2== 0:
        A = A*2
    else:
        B = B*2
print(A+B) 