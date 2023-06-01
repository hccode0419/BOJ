n = int(input())

first = 666
a = 0
while True:
    
    num = str(first)
    if '666' in num:
        a +=1
    if a == n:
        break
    first += 1
print(first)