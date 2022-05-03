#최대힙문제
#힙은 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진트리
# 파이썬 heapq는 최소힙으로 구현 되어있기에 입력받는 값에 음수 값을 곱해 push를 해주고 pop을 해주면 됨.

import sys
import heapq

heap = []
n = int(sys.stdin.readline())

for _ in range(n):
    m = int(sys.stdin.readline())
    if m == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-1*heapq.heappop(heap))
    else:
        heapq.heappush(heap,-1*m)