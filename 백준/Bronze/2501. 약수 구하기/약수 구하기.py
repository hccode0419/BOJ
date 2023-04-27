num, cnt = map(int, input().split())

lt = []
for i in range(1, num+1):
    if num % i == 0:   
        lt.append(i)

if len(lt) < cnt:
    print(0)
else:
    print(lt[cnt-1])
