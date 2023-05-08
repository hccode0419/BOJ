import sys
input=sys.stdin.readline
n=int(input())
arr={} # dic 선언 (현재 아무것도 없음)
for _ in range(n): # 
    k=int(input()) # key값을 입력함
    if k in arr.keys(): # dic의 키 값이 k에 있다면~
        arr[k]+=1 # 같은 key값이 있으면 value를 +1함 (반복하는 횟수를 추가함)
    else:
        arr[k]=1 #(처음에는 key값이 없으므로 이것이 실행됨) key : k 일때 value를 1로 선언
temp=list(arr.keys()) # key 값을 리스트로 받고 
temp.sort() # 정렬함
for i in temp: # key값을 i로 받고
    for _ in range(arr[i]): # key의 value의 값만큼 반복함(key가 중복될 때를 위해서)
        print(i) # key값을 출력함