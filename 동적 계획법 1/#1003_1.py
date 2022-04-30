# 쫌 더 쩌는 코드 발견......

import sys
read = sys.stdin.readline

cache = {0: [1,0], 1:[0,1]}
for i in range(2, 41):
    cache[i] = [cache[i-2][j] + cache[i-1][j] for j in range(2)]

T = int(read())
for _ in range(T):
    print(' '.join(map(str, cache[int(read())])))