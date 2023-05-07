import sys
input = sys.stdin.readline
n = int(input())

lt = []
for _ in range(n):
    a = int(input())
    if a != 0:
        lt.append(a)
    else:
        lt.pop()
print(sum(lt))
