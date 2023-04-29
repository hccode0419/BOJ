S = input()

for i in range(97, 123):
    if chr(i) in S:
        print(S.index(chr(i)), end=" ")
    elif chr(i) not in S:
        print(-1, end=" ")