#좌표정렬하기 문제

import sys
n = int(sys.stdin.readline())

coor_list = []
for _ in range(n):
    coor_list.append(list(map(int, sys.stdin.readline().split())))

coor_list.sort(key=lambda x: (x[0], x[1]))

for i in coor_list:
    print(i[0], i[1])