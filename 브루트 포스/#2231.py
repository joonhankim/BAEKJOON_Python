n = int(input())

for i in range(1,n+1):
    num = sum(map(int,str(i))) #각 자리수 더함
    num_sum = i + num #분해합
    if num_sum == n:
        print(i)
        break
    if i == n: #생성자가 없는 경우
        print(0)