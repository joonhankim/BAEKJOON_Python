#-와 - 사이의 수를 전부 괄호치면 끝!!!

arr = input().split('-') 
ans = 0 
for i in arr[0].split('+'): 
    ans += int(i) 
for i in arr[1:]: 
    for j in i.split('+'): 
        ans -= int(j) 
print(ans)
