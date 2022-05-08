import sys

def dfs(start,matrix):
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in matrix[start]:
        if d[i] == 0 or dfs(d[i],matrix):
            d[i] = start
            return 1
    return 0


if __name__ == '__main__':
    n,m = map(int,sys.stdin.readline().split())
    sys.setrecursionlimit(10 ** 9)


    matrix = [[] for _ in range(n + 1)]
    d = [0 for _ in range(m + 1)]

    cnt = 0

    for i in range(1, n + 1):
        a = list(map(int, sys.stdin.readline().split()))
        for j in a[1:]:
            matrix[i].append(j)

    for i in range(1, n + 1):
        visit = [0 for _ in range(n + 1)]
        if dfs(i,matrix):
            cnt += 1
    print(cnt)
