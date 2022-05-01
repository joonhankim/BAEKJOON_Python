#계단오르기 문제

import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+3)]
arr = [0 for _ in range(N+3)]

#계단 별 점수 정보 저장
for i in range(1,N+1):
    arr[i] = int(input())

#1번째 칸
dp[1] = arr[1]
#2번째 칸
dp[2] = arr[1]+arr[2]
#3번째 칸
dp[3] = max(arr[1]+arr[3],arr[2]+arr[3])

#마지막 계단의 관점에서 2개의 case로 나뉨!
for i in range(4,N+1):
    dp[i] = (max(dp[i-2]+arr[i],dp[i-3]+arr[i]+arr[i-1]))

print(dp[N])
