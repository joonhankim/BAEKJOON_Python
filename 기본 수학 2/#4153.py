#문제
# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오

while True:
    nums = list(map(int,input().split()))
    if sum(nums) == 0:
        break

    max_num = max(nums)
    nums.remove(max_num)
    if nums[0]**2 +nums[1]**2 == max_num**2:
        print("right")
    else:
        print('wrong')

#remove

