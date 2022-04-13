import sys
N = int(sys.stdin.readline())

for i in range(1,N+1):
    
    P = N-i

    K = " " * P
    J = "*" * i
    print(K+J)