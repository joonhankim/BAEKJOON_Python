import sys
from collections import defaultdict, deque

 
def dfs(cur):
    visited.add(cur)
 
    for next in forwardGraph[cur]:
        if next not in visited:
            dfs(next)
    stack.append(cur)
 
def reverseDfs(cur, scc):
    visited.add(cur)
    scc.append(cur)
 
    for next in reverseGraph[cur]:
        if next not in visited:
            scc = reverseDfs(next, scc)
    return scc
 
def kosaraju():
    global visited
    answer = []
    
    for i in range(1, V+1):
        if i not in visited:
            dfs(i)
 
    visited = set()
    while stack:
        scc = []
        cur = stack.pop()
 
        if cur in visited:
            continue
 
        answer.append(sorted(reverseDfs(cur, scc)))
    return answer

if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    V, E = map(int, sys.stdin.readline().split())
    forwardGraph = defaultdict(list)
    reverseGraph = defaultdict(list)
    
    for _ in range(E):
        A, B = map(int, sys.stdin.readline().split())
        forwardGraph[A].append(B)
        reverseGraph[B].append(A)
    
    stack = []
    visited = set()
    answer = kosaraju()
    
    print(len(answer))
    for line in sorted(answer):
        print(*line, sep = ' ', end = ' -1\n')
