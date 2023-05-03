L = int(input())
string = list(input())

total = 0
for idx, i in enumerate(string):
    a = (int(ord(i))-96)
    total = total + a * (31**int(idx))
print(total)
