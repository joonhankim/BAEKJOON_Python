import sys

if __name__ == '__main__':
    n,m = map(int,sys.stdin.readline().split())
    data = []
    result=[]
    
    for _ in range(n):
        data.append(list(map(str, sys.stdin.readline())))
    
    for i in range(0, n-7):
        for j in range(0, m-7):
            first_W = 0
            first_B = 0
            for x in range(i, i+8):
                for y in range(j, j+8):
                    if (x+y) % 2 == 0:
                        if data[x][y] != 'W':
                            first_W += 1
                        if data[x][y] != 'B':
                            first_B += 1
                    
                    else:
                        
                        if data[x][y] != 'W':
                            first_B += 1
                        
                        if data[x][y] != 'B':
                            first_W += 1
            result.append(first_W)
            result.append(first_B)

    print(min(result))