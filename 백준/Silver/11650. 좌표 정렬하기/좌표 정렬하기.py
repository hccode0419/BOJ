import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
arr.sort(key= lambda values : values[1])
arr.sort()
for i in arr: 
    print(*i)
