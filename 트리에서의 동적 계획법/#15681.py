import sys

def dfs(start_node,matrix,subtree,visited_list):
    subtree[start_node] = 1
    visited_list[start_node] = 1
    for i in matrix[start_node]:
        if visited_list[i] == 0:
            dfs(i,matrix,subtree,visited_list)
            subtree[start_node] += subtree[i]
    return subtree

if __name__ == '__main__':
    n, r, q = map(int,sys.stdin.readline().split())
    sys.setrecursionlimit(10 ** 9)

    matrix = [[] for _ in range(n+1)] 
    visited_list,subtree = [0]*(n+1) , [0]*(n+1)

    for _ in range(n-1): 
        x, y = map(int, sys.stdin.readline().split()) 
        matrix[x].append(y) 
        matrix[y].append(x)

    result_subtree = dfs(r,matrix,subtree,visited_list)

    for _ in range(q): 
        print(result_subtree[int(sys.stdin.readline())])