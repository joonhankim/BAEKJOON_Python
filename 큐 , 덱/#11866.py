import sys 
from collections import deque 




if __name__ == '__main__':
    n,k = map(int,sys.stdin.readline().split())
    queue = deque([])
    result = []
    for i in range(1, n+1):
        queue.append(i)

    while queue:
        for _ in range(k-1):
            queue.append(queue.popleft())
        result.append(queue.popleft())

    print('<',end='')
    print(*result,sep=', ',end='')
    print('>')