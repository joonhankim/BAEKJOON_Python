#소트인사이드 문제

import sys

n = int(sys.stdin.readline())

num_list = []

for chr in str(n):
    num_list.append(int(chr))

num_list.sort(reverse=True)

print(''.join(map(str, num_list)))