def dfs(x,y):
    global cnt
    if x<0 or x>=n or y<0 or y>=n: 
        return False
    
    if matrix[x][y]==1:
        cnt +=1
        matrix[x][y] = 0
        for i in range(4):
            dfs(x+dx[i],y+dy[i])
        return True

if __name__ == '__main__':

    n = int(input())
    matrix = []

    for _ in range(n):
        matrix.append(list(map(int,input())))
    
    grp = []
    cnt = 0
    dx = [-1,1,0,0] 
    dy = [0,0,-1,1]

    for i in range(n):
        for j in range(n):
            if dfs(i,j)==True:
                grp.append(cnt)
                cnt = 0
    
    print(len(grp))
    
    grp.sort()
    for i in grp:
        print(i)