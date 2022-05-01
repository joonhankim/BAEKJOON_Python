#색종이 만들기 문제
#분할 정복(쿼드트리)
#재귀함수 사용 + 조건 걸리면 4분기

import sys
n=int(sys.stdin.readline())

color_paper= []
for _ in range(n):
    color_paper.append(list(map(int,sys.stdin.readline().split())))

white = 0
blue = 0

#함수 파라미터: x,y좌표 그리고 한변의 길이
def cut(x,y,n):
    global blue,white
    check_color=color_paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check_color!=color_paper[i][j]:#하나라도 같은색이 아니라면
                #4등분
                cut(x,y,n//2)#1사분면
                cut(x,y+n//2,n//2)#2사분면
                cut(x+n//2,y,n//2)#3사분면
                cut(x+n//2,y+n//2,n//2)#4사분면
                return
 
 
    if check_color==0:#모두 흰색일때
        white+=1
        return
    else:   #모두 파란색일때
        blue+=1
        return
 
 
cut(0,0,n)
print(white)
print(blue)