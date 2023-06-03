from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())
arr = []
arr_max = []
def arithmetic_mean(arr):
    return round(sum(arr) / len(arr))
def center(arr):
    return arr[len(arr)//2]
def get_mode(arr):
    counts = Counter(arr)
    mode_values = counts.most_common()
    if len(mode_values) > 1 and mode_values[0][1] == mode_values[1][1]:
        return mode_values[1][0]
    else:
        return mode_values[0][0]
def rg(arr):
    M_arr = arr[-1]
    m_arr = arr[0]
    return M_arr-m_arr
for _ in range(N):
    arr.append(int(input()))
arr.sort()

print(arithmetic_mean(arr))
print(center(arr))
print(get_mode(arr))
print(rg(arr))