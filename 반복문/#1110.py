import sys

N = int(sys.stdin.readline())

i = 0
while True:
    ten_N = N // 10 
    one_N = N % 10 
    if (ten_N + one_N) // 10 == 0:
        new = one_N * 10 + one_N
        
    else:
        sum_N = (ten_N + one_N) % 10
        new = one_N * 10 + sum_N
        
    i+=1
    if new == N :
        print(i)
        break
    else:
        N = new
#아직 진행중..;;;;;