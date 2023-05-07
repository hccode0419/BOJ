##### 분해합 - > 생성자
import sys
input = sys.stdin.readline

N = int(input())

L = []
for i in range(1, N+1):
    a = i
    i = list(map(int, str(i))) # int형을 각 자리수의 list로 변환 ex) 123 =>[1, 2, 3]
    for j in range(len(i)):
        a = a + int(i[j])
    if a == N:
        L.append(i)
if len(L) == 0:
    print(0)
else: # to-do : [[1, 9, 8],[2, 0, 7]] 첫번째 리스트의 각 자리수를 더하는 것 
    int_L = []
    for i in range(len(L)):
        b = str(L[i][0])
        len_i = len(L[i])
        for j in range(1, len_i):
            b =  b + str(L[i][j])
        int_L.append(b)
    lnt_N_L = list(map(int, int_L)) # 문자열을 int로 반환
    print(min(lnt_N_L))
