import sys

def floyd(n,matrix):
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                matrix[j][k] = min(matrix[j][k],matrix[j][i]+matrix[i][k])
    return matrix

if __name__ == '__main__':
    n,m = map(int, sys.stdin.readline().split())

    INF = int(1e9)

    matrix = [[INF] * (n+1) for _ in range(n+1)]

    for x in range(1,n+1):
        for y in range(1,n+1):
            if x == y:
                matrix[x][y] = 0
    
    for _ in range(m):
        x,y,z = map(int, sys.stdin.readline().rstrip().split())
        if matrix[x][y] > z :
            matrix[x][y] = z

    result_matrix = floyd(n,matrix)

    for x in range(1,n+1):
        for y in range(1,n+1):
            if result_matrix[x][y] == INF:
                print(0, end = " ")
            else:
                print(result_matrix[x][y], end = " ")
        print()
