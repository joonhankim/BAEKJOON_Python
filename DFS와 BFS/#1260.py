import sys

def dfs(start_node):
    check_visited_for_dfs[start_node] = 1
    print(start_node,end=' ')
    for i in range(1,n+1):
        if matrix[start_node][i] == 1 and check_visited_for_dfs[i] == 0:
            dfs(i)
    return True

def bfs(start_node):
    queue = [start_node]
    check_visited_for_bfs[start_node] = 1
    while queue:
        start_node = queue.pop(0)
        print(start_node, end=' ')
        for i in range(1,n+1):
            if matrix[start_node][i] == 1 and check_visited_for_bfs[i] == 0:
                queue.append(i)
                check_visited_for_bfs[i] = 1
    return True

if __name__ == '__main__':
    n, m, v = map(int, sys.stdin.readline().split())

    matrix = [[0] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        x,y = map(int, sys.stdin.readline().split())
        matrix[x][y] = matrix[y][x] = 1

    check_visited_for_dfs = [0]*(n+1)
    check_visited_for_bfs = check_visited_for_dfs.copy()

    dfs(v)
    print()
    bfs(v)