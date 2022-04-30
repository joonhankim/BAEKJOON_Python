#N-Queen문제
#패스트캠퍼스 강의 도움 받음!

import sys

N = int(sys.stdin.readline())

#수직체크, 대각선체크
def is_available(candidate,current_col):
    current_row = len(candidate)
    # 현재 행이 2행이면 0,1,2
    for queen_row in range(current_row):
        #candidate[queen_row] == queen의 col
        if candidate[queen_row] == current_col or abs(candidate[queen_row]-current_col) == current_row - queen_row:
            return False
    return True

def DFS(N,current_row,current_candidate,final_result):
    # 종료조건 (조건에 다 맞아서 N개의 배치가 끝났다)
    if current_row == N:
        # 지금까지 결과가 다 저장되었다 # shallow copy
        final_result.append(current_candidate[:])
        return
    #그렇지 않고 중간행이라면,
    for candidate_col in range(N):
        # 이게 프루닝(조건체크)
        if is_available(current_candidate,candidate_col):
            #만족이 됬다라고 하면 일단 넣어줘
            current_candidate.append(candidate_col)
            #다음행에 , 그전까지 배치된 정보 넘겨주고
            DFS(N,current_row+1,current_candidate,final_result)
            #가장 최근에 append 된 것이 없어짐 [:-1]
            current_candidate.pop()

def solve_n_queens(N):
    final_result = []
    DFS(N,0,[],final_result)
    return final_result