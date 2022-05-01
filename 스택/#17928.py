import sys
from collections import deque

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

stack = deque()
result = [-1 for _ in range(n)]

for i in range(n): 
    while stack and stack[-1][0] < arr[i]: 
        tmp, idx = stack.pop()
        result[idx] = arr[i] 
    stack.append([arr[i],i])

#파이썬에서 배열을 print할 때, 앞에 *을 붙여주면 공백을 기준으로 원소들만 나열
print(*result)