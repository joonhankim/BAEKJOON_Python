import sys
import random
N,X= 10,5

number_list = list(range(1,N+1))
random.shuffle(number_list)

result = list()
for num in number_list:
    if num < X :
        result.append(num)

print(result)