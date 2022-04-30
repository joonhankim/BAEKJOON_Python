# 재귀함수를 사용하면 시간이 너무 오래걸림
# 동적 계획법을 사용해야함 (메모라이징)
#계산한 값을 중간에 확인하는 분기를 주면, 불필요한 계산을 줄이고 이전에 계산한 값을 사용할 수 있음.

import sys

cache = {}

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    # if a<b<c:
    #     return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    key = '{} {} {}'.format(a, b, c)

    #계산한 값을 중간에 확인하는 분기 (메모라이징)
    if key in cache:
        return cache[key]
    res = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    cache[key] = res

    return res

while True:
    a,b,c = map(int,sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))