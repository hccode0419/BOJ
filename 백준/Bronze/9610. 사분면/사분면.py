N = int(input())

cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt0 = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a == 0 or b == 0:
        cnt0 +=1
    elif a > 0 and b > 0:
        cnt1 +=1
    elif a < 0 and b > 0:
        cnt2 +=1
    elif a < 0 and b < 0:
        cnt3 +=1
    elif a > 0 and b < 0:
        cnt4 +=1
print("Q1:", cnt1)
print("Q2:", cnt2)
print("Q3:", cnt3)
print("Q4:", cnt4)
print("AXIS:", cnt0)