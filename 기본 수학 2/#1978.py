#소수찾기

n = int(input()) #not used
nums = map(int, input().split())

sosu_count = 0
for num in nums:
    bug = 0
    if num > 1 :
        for i in range(2, num):  
            if num % i == 0:
                bug += 1  
        if bug == 0:
            sosu_count += 1  

print(sosu_count)