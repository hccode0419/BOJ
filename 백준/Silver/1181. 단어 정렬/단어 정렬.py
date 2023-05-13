n = int(input())
arr = []
for i in range(n):
    word = input()
    arr.append((word, len(word)))
seted_arr = list(set(arr))
seted_arr.sort()
seted_arr.sort(key = lambda x: x[1])

for i in range(len(seted_arr)):
    print(seted_arr[i][0])