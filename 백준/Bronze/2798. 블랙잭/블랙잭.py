n, m = map(int, input().split())

nums = list(map(int, input().split()))

nums.reverse()


mx = 0

for i in range(n):
    for j in range(i+1 , n):
        for k in range(j+1, n):
            sum = nums[i] + nums[j] + nums[k]
            if sum <= m:
                if mx < sum:
                    mx = sum                     
                
print(mx)