#벌집문제

n = int(input())

house_num = 1  
cnt = 1
while n > house_num :
    house_num += 6 * cnt  
    cnt += 1  
print(cnt)

