N = int(input())
arr = []

for i in range(N):
    values = input().split()
    age = int(values[0])

    arr.append([age, values[1]])

sorted_dict = sorted(arr, key = lambda item: item[0])
for i in range(N):
    print(sorted_dict[i][0], sorted_dict[i][1])