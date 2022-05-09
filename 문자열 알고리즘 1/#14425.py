import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    string_set = [str(sys.stdin.readline()) for _ in range(n)]
    # string_set = []
    # for _ in range(n):
    #     string = str(sys.stdin.readline())
    #     string_set.append(string)

    cnt = 0
    
    for _ in range(m):
        word = str(sys.stdin.readline())
        if word in string_set:
            cnt += 1

    print(cnt)

