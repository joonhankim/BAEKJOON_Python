#통계학문제

import sys
from collections import Counter

n = int(sys.stdin.readline())

nums = []
#nums 리스트에 일단 append... 시간이 초과되려나...
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
#순서대로 정렬
nums.sort()
count_nums = Counter(nums).most_common()

#For 산술평균
print(round(sum(nums) / n))

#For 중앙값
print(nums[n // 2])

#For 최빈값
if len(count_nums) > 1:
    if count_nums[0][1] == count_nums[1][1]:
        print(count_nums[1][0])
    else:
        print(count_nums[0][0]) #else안쓰는 방법은 없을까
else:
    print(count_nums[0][0])

#For 범위
print(nums[-1] - nums[0])