Num = [int(input()) for _ in range(10)]  
rest_list = [Num[i]%42 for i in range(10)]

result = set(rest_list)
print(len(result))
