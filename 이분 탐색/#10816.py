# 이전 문제에서 크게 바꾼게 없어서 편했던 문제
#하지만 sys안써서 시간 오지게 오래 걸림...3876ms

def binary_search(a,x,start,end):
    if start > end:
        return 0
    mid = (start+end)//2
    
    if x == a[mid]:
        return a[start:end+1].count(x)
    elif x < a[mid]:
        return binary_search(a,x,start,mid-1)
    else:
        return binary_search(a,x,mid+1,end)

n = int(input())
a= list(map(int,input().split()))
a= sorted(a)

m = int(input())
m_l = list(map(int,input().split()))

n_dic = {}
for m in m_l:
    if m not in n_dic:
        n_dic[m] = binary_search(a,m,0,n-1)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in m_l ))