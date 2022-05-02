import sys

N = int(sys.stdin.readline())

image = [list(map(int, sys.stdin.readline())) for _ in range(N)]

def compression(x,y,n):
    check = image[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            #하나라도 다르면
            if check!=image[i][j]:
                #4등분
                print('(', end='')
                compression(x,y,n//2)#1사분면
                compression(x,y+n//2,n//2) #2사분면
                compression(x+n//2,y,n//2)  #3사분면
                compression(x+n//2,y+n//2,n//2)#4사분면
                print(')', end='')
                return
 
    #모두 0일때 
    if check==0:
        print('0',end='')
        return
    #모두 1일때
    else:   
        print('1',end='')
        return
 
 
compression(0,0,N)