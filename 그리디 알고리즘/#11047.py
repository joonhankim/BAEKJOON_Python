#굳이 sys 안씀! (68ms소요)
N, K = map(int, input().split()) 

# 동전들 리스트에 입력 받고 오름차순을 내림차순으로 변경 (for greedt algorithm)
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)

answer = 0
for coin in coins:
    if K >= coin:
        #목만큼 더하기
        answer += K // coin 
        # 나눈 나머지 할당
        K %= coin 
        if K <= 0: 
       		break
print(answer) 