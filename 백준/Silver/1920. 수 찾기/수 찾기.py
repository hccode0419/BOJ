
import sys
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

N = int(sys.stdin.readline())
data_list = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
target_list = list(map(int, sys.stdin.readline().split()))
s = ''
for i in range(M):
    if binary_search(data_list, target_list[i]):
        s += '1\n'
    else:
        s += '0\n'
print(s)

