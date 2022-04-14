import sys

N = int(sys.stdin.readline())

check = N
new_N = 0
temp = 0
count = 0

while True:
    temp = (N//10) + (N%10)
    new_N = (N%10)*10 + temp%10
    count += 1
    N = new_N
    if new_N == check:
        break
print(count)