import math
import sys

input = sys.stdin.readline

N = list(map(int,input().split()))
N_list = []
for i in range(1,max(N)+1):
    if N[0]%i == 0 and N[1]%i == 0 :
        N_list.append(i)
result = max(N_list)
K = math.trunc(N[0]*N[1]/result)

print(result)
print(K)
