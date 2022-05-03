#heap에 push를 할 때 (절댓값, 원래값)을 같이 넣어줘서 
#만약 절댓값이 같으면 원래 값이 음수인 것이 먼저 출력되게 해줌.
#pop을 해줄 때는 heapq.heappop(heap)[1]로 해서 뒤에 있는 원래 값을 출력

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
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(abs(m),m))