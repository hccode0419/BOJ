import sys
input = sys.stdin.readline

N = int(input())
lt = []

for i in range(N):
    a = input().split()
    if a[0] == "push_front":
        lt.append(int(a[1]))
    elif a[0] == "push_back":
        lt.insert(0, int(a[1]))
    elif a[0] == "pop_front":
        if len(lt) > 0:
            p = lt.pop()
            print(p)
        else:
            print(-1)
    elif a[0] == "pop_back":
        if len(lt) > 0:
            p = lt.pop(0)
            print(p)
        else:
            print(-1)
    elif a[0] == "size":
        print(len(lt))
    elif a[0] == "empty":
        if len(lt) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if len(lt) == 0:
            print(-1)
        else:
            print(lt[-1])
    elif a[0] == "back":
        if len(lt) == 0:
            print(-1)
        else:
            print(lt[0])

