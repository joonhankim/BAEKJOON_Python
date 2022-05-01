#평범한 배낭 문제

import sys
n,k = map(int,sys.stdin.readline().split())

#테이블 초기화
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1,n+1):
    weight, value = map(int,sys.stdin.readline().split())
    for j in range(1,k+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight]+value)

print(dp[n][k])
