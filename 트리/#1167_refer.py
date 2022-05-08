import sys

def dfs(start_node, matrix, visited_list):
    for x, y in matrix[start_node]:
        if visited_list[x] == 0:
            visited_list[x] = visited_list[start_node]+y
            dfs(x, matrix, visited_list)
    return visited_list

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    sys.setrecursionlimit(10**6)
    matrix = [[] for _ in range(n+1)]

    visited_list = [0] * (n+1)

    for i in range(n):
        path = list(map(int, sys.stdin.readline().split()))
        path_len = len(path)
        for i in range(1, path_len//2):
            matrix[path[0]].append([path[2*i-1], path[2*i]])
    
    resul_visited_list = dfs(1, matrix, visited_list)

    resul_visited_list[1] = 0

    tmpmax = 0 
    index = 0 
    
    for i in range(len(resul_visited_list)):
        if tmpmax < resul_visited_list[i]:
            tmpmax = resul_visited_list[i]
            index = i
    
    result_final = [0 for _ in range(n+1)]
    final_visited_list = dfs(index, matrix, result_final)
    final_visited_list[index] = 0
    print(max(final_visited_list))