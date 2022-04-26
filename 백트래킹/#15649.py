#N과 M(1)

n, m = map(int, input().split())

visited = [False] * n #탐사 여부 체크
out = [] #출력내용

def solve(depth,n,m):
    if depth == m: #탈출조건
        print(' '.join(map(str,out))) #list를 str로 합쳐 출력.
        return
    for i in range(len(visited)): #탐사 체크하면서
        if not visited[i]: #탐사 안했다면
            visited[i] = True
            out.append(i+1) #탐사내용
            solve(depth+1,n,m) #깊이 우선 탐색
            visited[i] = False
            out.pop() #탐사내용 제거

solve(0,n,m)


