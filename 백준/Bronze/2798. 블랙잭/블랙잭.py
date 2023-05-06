N, M = map(int, input().split())
L = list(map(int, input().split()))

sum_L = []
for i in range(len(L)-2):
    for j in range(i+1, len(L)-1):
        for k in range(j+1, len(L)):
            a = L[i] + L[j] + L[k]
            if a < M+1:
                sum_L.append(a)
                
print(max(sum_L))