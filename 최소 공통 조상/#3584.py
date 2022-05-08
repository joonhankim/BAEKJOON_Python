import sys

def find_parent(parent_list, node):
    patent_list_of_node = [node]
    while parent_list[node]:
        patent_list_of_node.append(parent_list[node])
        node = parent_list[node]
    return patent_list_of_node

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        parent_list = [0 for _ in range(n+1)]
        for _ in range(n-1):
            x, y = map(int, input().split())
            parent_list[y] = x
        
        x, y = map(int, sys.stdin.readline().split())
    
        parent_list_of_x = find_parent(parent_list, x)
        parent_list_of_y = find_parent(parent_list, y)
        
        spot_of_x = len(parent_list_of_x)-1
        spot_of_y = len(parent_list_of_y)-1
        
        while parent_list_of_x[spot_of_x] == parent_list_of_y[spot_of_y]:
            spot_of_x-=1
            spot_of_y-=1

        print(parent_list_of_x[spot_of_x+1])