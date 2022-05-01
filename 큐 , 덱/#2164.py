import sys 
from collections import deque 

N = int(sys.stdin.readline()) 
queue = deque() 

#1234 만들기
for i in range(N): 
    queue.append(i + 1) 

 
while len(queue) > 1: 
    #일단 1을 버리고
    queue.popleft() 
    #342
    queue.append(queue.popleft()) 
    
print(queue.pop())
