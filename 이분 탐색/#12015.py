import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
A = [*map(int, sys.stdin.readline().split())]

LIS = [A[0]]

for num in A:
    if LIS[-1] < num:
        LIS.append(num)
    else:
        idx = bisect_left(LIS, num)
        LIS[idx] = num

print(len(LIS))