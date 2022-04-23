# #문제
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

n = int(input())

for _ in range(n):
    cnt, word = input().split()
    for i in word:
        print(i*int(cnt),end='')
    print()

#문자열을 iterable 자리에 입력하면 문자열의 각 문자를 분리해서 변수에 선언
#print 함수에서 end 파라미터를 이용하지 않을 때는 줄 넘김 기능이 기본값이고 print 함수 안에서 출력할 값이 여러 개인 경우 공백으로 출력 값이 구분
