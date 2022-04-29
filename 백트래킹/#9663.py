#N-Queen문제
#어렵다 은근(계속 시간초과가 뜸 ㅜㅜ)
import sys

n = int(sys.stdin.readline())
board = [0] * n
ans = 0

def check(r,c):
    for row in range(r):
        if c == board[row]:
            return False
        if r - c == row - board[row]:
            return False
        if r+c == row + board[row]:
            return False
    return True

def backtrack(idx):
    global ans
    if idx == n:
        ans+=1
    else:
        for i in range(n):
            if check(idx,i):
                board[idx] = i
                backtrack(idx+1)
                board[idx] = 0


backtrack(0)
print(ans)