N = int(input())
A = list(map(int, input().split()))

P_num = 0
for num in A:
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 n-1까지
            if num % i == 0:
                error += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
        if error == 0:
            P_num += 1  # error가 없으면 소수.
print(P_num)