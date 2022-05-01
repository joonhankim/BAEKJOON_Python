#ATM 문제
#애는 좀 많이 쉬웠다..ㅎㅎ

N = int(input())
people = list(map(int, input().split()))

people.sort(reverse=True)

answerM = 0

for i in range(1,N+1):
    answerM += sum(people[0:i])

print(answerM)