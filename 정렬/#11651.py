import sys

n = int(sys.stdin.readline())

coor_list = []
for _ in range(n):
    [x,y] = map(int,sys.stdin.readline().split())
    coor_list.append([y,x])

coor_list = sorted(coor_list)

for y,x in coor_list:
    print(x,y)