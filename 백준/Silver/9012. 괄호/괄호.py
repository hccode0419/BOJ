T = int(input())

for _ in range(T):
    PS = list(input())
    cnt_left = 0
    cnt_right = 0
    VPS = True
    if PS.count("(") != PS.count(")"):
        VPS = False
    elif PS[-1] == "(":
        VPS = False
    elif PS[0] != "(":
        VPS = False
    for j in range(len(PS)):
        if PS[j] == '(':
            cnt_left += 1
        elif PS[j] == ')':
            cnt_right += 1
        if cnt_left < cnt_right:
            VPS = False
    if VPS:
        print("YES")
    else:
        print("NO")
