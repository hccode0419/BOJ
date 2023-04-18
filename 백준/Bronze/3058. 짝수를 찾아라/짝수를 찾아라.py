n = int(input())

    

L = [map(int, input().split()) for i in range(n)]
for i in range(len(L)):
    L_even = []
    for j in L[i]:
        if j % 2 ==0:    
            L_even.append(j)
    print(sum(L_even), min(L_even))
    