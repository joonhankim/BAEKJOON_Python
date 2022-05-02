#import sys에는 문제가 있다 (런타임 에러 계속 뜸;;;)

def binary_search(a,x,start,end):
    if start > end:
        return 0
    mid = (start+end)//2

    if x == a[mid]:
        return 1
    elif x < a[mid]:
        return binary_search(a,x,start,mid-1)
    else:
        return binary_search(a,x,mid+1,end)

n = int(input())
a= list(map(int,input().split()))
a= sorted(a)

m = int(input())
m_l = list(map(int,input().split()))

for m in m_l:
    if binary_search(a,m,0,n-1):
        print(1)
    else:
        print(0)