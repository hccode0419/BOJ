import sys
input = sys.stdin.readline

m , n = map(int, input().split())

for i in range(m, n+1):
    cnt = True
    if i == 1:
        cnt = False
        continue
    for j in range(2, int(i**(1/2))+1):
        if i % j == 0:
            cnt = False
            break
    
    if cnt:
        print(i)
