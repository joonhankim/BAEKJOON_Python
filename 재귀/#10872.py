#문제
#0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

n = int(input())

def factorial(num:int):
    if num == 0:
        return 1
    return num * factorial(num-1)

print(factorial(n))