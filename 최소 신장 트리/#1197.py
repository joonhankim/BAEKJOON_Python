import sys

def find_root_node(element,parent_table):
    if element == parent_table[element]: 
        return element
    parent_table[element] = find_root_node(parent_table[element],parent_table) 
    return parent_table[element]

def union_find(element_a,element_b,parent_table):
    root_a = find_root_node(element_a,parent_table) 
    root_b = find_root_node(element_b,parent_table) 
    if root_a == root_b: 
        return True
    if root_a < root_b: 
        parent_table[root_b] = root_a
    else:
        parent_table[root_a] = root_b
    return True

if __name__ == '__main__':
    n,m = map(int,sys.stdin.readline().split())
    sys.setrecursionlimit(10**6)
    parent_table= [0] * (n+1) 

    for i in range(n+1): 
        parent_table[i] = i
    
    matrix = []

    for _ in range(m):
        a,b,c = map(int,sys.stdin.readline().split())
        matrix.append([c,a,b])

    matrix.sort()

    sum = 0
    for c, a, b in matrix:
        if find_root_node(a,parent_table) != find_root_node(b,parent_table):
            union_find(a, b,parent_table)
            sum += c

    print(sum)
