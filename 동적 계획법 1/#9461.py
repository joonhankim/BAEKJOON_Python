#파도반 수열
#P[N] = P[N-3] +P[N-2]

import sys

T = int(sys.stdin.readline())

# DP 테이블 초기화
P = [0 for i in range(101)]

#공식에 벗어나기에 미리 지정
P[1] = 1
P[2] = 1
P[3] = 1

# bottom-up 방식
for i in range(4,101):
    P[i] = P[i-3]+P[i-2]

for _ in range(T):
    a = int(sys.stdin.readline())
    print(P[a])