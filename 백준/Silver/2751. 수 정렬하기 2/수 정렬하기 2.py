import sys
input = sys.stdin.readline
N = int(input())
L = []
if 1 <= N <= 1000000: 
    for _ in range(N):
        a = int(input())
        L.append(a)
    L.sort()
    if -1000000 <= a <= 1000000:
        for i in L:
            print(i)
