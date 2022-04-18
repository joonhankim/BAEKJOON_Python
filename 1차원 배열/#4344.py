#문제
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

C = int(input())


for i in range(C):
    score_list = list(map(int,input().split()))
    av = sum(score_list[1:]) / score_list[0]
    port = 0
    for score in score_list[1:]:
        if score > av:
            port +=1

    result = (port/score_list[0]) *100

    print("%.3f" % result +'%')
