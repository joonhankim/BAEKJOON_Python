import sys

def hanoi_recursive(n,start,middle,end):
    if n == 1:
        print(start,end)
    else:
        hanoi_recursive(n-1,start,end,middle)
        print(start,end)
        hanoi_recursive(n-1,middle,start,end)
    
    return True

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    # sys.setrecursionlimit(10**6)
    print(2**n -1)
    hanoi_recursive(n,1,2,3)