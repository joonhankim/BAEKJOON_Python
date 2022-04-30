#피보나치 함수

import sys

T = int(sys.stdin.readline())

# 0과 1은 고정값을 가진 리스트를 만들어 놓는다.
zero = [1,0,1]
one = [0,1,1]

def fibo_dp(n):
    if len(zero) <= n:
        for i in range(len(zero),n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n],one[n])

for _ in range(T):
    a = int(sys.stdin.readline())
    fibo_dp(a)




