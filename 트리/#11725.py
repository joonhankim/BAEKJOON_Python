import sys

def dfs(start_node,matrix,visited_list):
    for i in matrix[start_node]:
        if visited_list[i] == 0:
            visited_list[i] = start_node
            dfs(i,matrix,visited_list)
    return visited_list


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    matrix = [[] for _ in range(n+1)]

    for i in range(n-1): 
        x, y = map(int, sys.stdin.readline().split()) 
        matrix[x].append(y) 
        matrix[y].append(x)

    visited_list = [0] * (n+1)

    arr = []

    result_visited_list = dfs(1,matrix,visited_list)

    for i in range(2,n+1):
        print(visited_list[i])