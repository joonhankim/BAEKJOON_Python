#카운팅정렬문제

import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

#for문 속에서 append()를 사용하게 되면 메모리 재할당이 이루어져서 메모리를 효율적으로 사용못함.
for _ in range(n):
    #인덱스를 하나씩 증가.
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for _ in range(num_list[i]):
            print(i)
