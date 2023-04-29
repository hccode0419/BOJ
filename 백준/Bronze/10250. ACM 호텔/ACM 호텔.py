T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    if N <= H:
        print(100*N + 1)
    elif  N > H:
        if N % H == 0:
            print(H*100 + N//H)
        else:
            print((N % H) *100 +((N // H)+1)) # 나머지 : 층/ 몫+1: 호
