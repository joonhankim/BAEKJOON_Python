# 정수 삼각형 문제
# 위층에서 아래층으로 내려갈 수 있는 모든 경우의 수 중에 max 값을 뽑아내면 된다.


import sys
n= int(sys.stdin.readline())

dp = []
for _ in range(n):
    dp.append(list(map(int,sys.stdin.readline().split())))


for i in range(1,n):
  for j in range(len(dp[i])):
    if j==0:
      dp[i][j]+=(dp[i-1][j])
    elif i == j: 
      dp[i][j]+=(dp[i-1][j-1])
    else:
      dp[i][j]+=(max(dp[i-1][j-1],dp[i-1][j]))

print(max(dp[n-1]))