import sys
n = int(input())
a = list(sys.stdin.readline())
b = 0
for i in range(1, n+1):
    for j in range(i-1, i):
        b = b + int(a[j])
print(b)

