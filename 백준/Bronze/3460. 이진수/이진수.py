import sys
input = sys.stdin.readline
n= int(input())

for _ in range(n):
    num = int(input())
    L = []
    while num > 0:
        if num % 2 == 1:
            L.append(1)
            num = num // 2
        elif num % 2 ==0:
            L.append(0)
            num = num // 2
    for i in range(len(L)):
        if L[i] == 1:
            print(L.index(1), end=' ')
        L[i] = 0
    print() 