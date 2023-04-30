import sys
input = sys.stdin.readline
N = int(input())

dice_list = [0]*N
for i in range(N):
    a, b, c = map(int, input().split())
    if a == b == c:
        money = 10000 + a*1000
        dice_list[i] = money
    elif a == b:
        money = 1000 + a*100
        dice_list[i] = money
    elif b == c:
        money = 1000 + b*100
        dice_list[i] = money
    elif a == c:
        money = 1000 + a*100
        dice_list[i] = money
    else:
        money = max(a, b, c)*100
        dice_list[i] = money
print(max(dice_list))
