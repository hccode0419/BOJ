while True:
    LT = list(map(int,input().split()))
    N_LT = sorted(LT)
    a = N_LT[0]
    b = N_LT[1]
    c = N_LT[2]
    if a == 0 and b==0 and c == 0:
        break
    elif a**2 + b**2 == c**2 and a !=0:
        print("right")
    elif a**2 + b**2 != c**2:
        print("wrong")
