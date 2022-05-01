import sys

t = int(sys.stdin.readline())

for i in range(t):
    b = sys.stdin.readline()
    s = list(b)
    sum = 0
    for i in s:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        #-1이 되면 탈출
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    #vps
    elif sum == 0:
        print('YES')