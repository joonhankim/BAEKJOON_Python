#제로문제

import sys

k = int(sys.stdin.readline())

num_list = []
for _ in range(k):
    a = int(sys.stdin.readline())
    if a == 0:
        num_list.pop()
    else:
        num_list.append(a)
    
print(sum(num_list))