import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    numbers = sorted(list(map(int, sys.stdin.readline().split())))
    x = int(sys.stdin.readline())

    answer = 0
    left, right = 0, n-1 
    while left != right:
        if numbers[left] + numbers[right] == x:
            answer+=1
            left+=1
        elif numbers[left] + numbers[right] > x:
            right -=1
        else:
            left+=1
    print(answer)