# 이건 시간초과 때문에 sys 써야겠다..!
# mid로 나눈다........

import sys
K, N = map(int,sys.stdin.readline().split())
lans = [int(sys.stdin.readline()) for _ in range(K)]

start, end = 1, max(lans)

def binary_search(start, end, N):
    if start > end:
        return end
    
    mid = (start + end) // 2

    lines = 0

    ####이게 핵심############
    for lan in lans:
        lines += lan // mid
    ######################

    if lines >= N:
        return binary_search(mid+1, end, N)
    else:
        return binary_search(start, mid-1, N)

print(binary_search(start, end, N))

