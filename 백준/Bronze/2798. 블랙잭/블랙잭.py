n, m = map(int, input().split())

nums = list(map(int, input().split()))


nums = sorted(nums)

L = []
for i in range(n):
    for j in range(i+1 , n):
        for k in range(j+1, n):
            sum = nums[i] + nums[j] + nums[k]
            if sum <= m:
                L.append(sum)
                     

print(max(L))