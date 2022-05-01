#-와 - 사이의 수를 전부 괄호치면 끝!!!

arr = input().split('-') 
s = 0 
for i in arr[0].split('+'): 
    s += int(i) 
for i in arr[1:]: 
    for j in i.split('+'): 
        s -= int(j) 
print(s)

