def dfs(matrix, v, visited_list):
    global cnt
    visited_list[v] = 1
    for i in matrix[v]:
        if not visited_list[i]:
            cnt += 1
            dfs(matrix, i, visited_list)
    return True

if __name__ == '__main__':

    num_of_com = int(input())
    num_of_com_pair = int(input())

    matrix = [[] for _ in range(num_of_com + 1)]
    
    for _ in range(num_of_com_pair):
        x,y = map(int, input().split())
        matrix[x].append(y)
        matrix[y].append(x)

    check_visited_for_dfs = [0]*(num_of_com+1)
    cnt = 0
    dfs(matrix, 1, check_visited_for_dfs)
    print(cnt)