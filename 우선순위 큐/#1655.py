# 힙을 두개 쓰자...(하.. 이런 생각은 왜 못하는가...!!)
#왼쪽 힙은 최대 힙으로 정렬, 오른쪽 힙은 최소 힙으로 정렬하면
# 왼쪽 힙의 첫번쨰 요소는 항상 중앙값이 된다는 사실.....!
#중간값보다 작은 값들은 leftHeap에, 큰 값은 rightHeap에 저장

import sys
import heapq

leftHeap,rightHeap = [],[]

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)
    
    # 오른쪽 힙에 원소를 넣는 차례에 왼쪽 힙보다 작은 값을 넣게 된다면,
    # 오른쪽 힙에 중간값보다 큰 원소가 들어가게 되므로
    # 왼쪽 힙의 첫번째 원소와 오른쪽 힙의 첫번째 원소를 교체하여 균형을 유지한다.
    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)

    print(-leftHeap[0])