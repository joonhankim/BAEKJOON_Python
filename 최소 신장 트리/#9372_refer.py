import sys

if __name__ == '__main__':
    for t in range(int(input())):
        N, M = map(int, input().split())
        for i in range(M):
            a, b = map(int, sys.stdin.readline().split())

        print(N-1)