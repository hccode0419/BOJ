import sys
input = sys.stdin.readline

N = int(input())
lst= []
a = 0
for i in range(N):
    i_list = list(map(int, str(i)))
    S = sum(i_list) + i
    if S == N:
        a = 1
    if a == 1:
        print(i)
        break
if a == 0:
    print(0)
    
