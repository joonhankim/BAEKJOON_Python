# import sys

# N = 26


# i = 0
# while True:
#     ten_N = N // 10 
#     one_N = N % 10 
#     if (ten_N + one_N) // 10 == 0:
#         new = one_N * 10 + one_N
#         print("yes",new)
#     else:
#         sum_N = (ten_N + one_N) % 10
#         new = one_N * 10 + sum_N
#         print("no",new)
#     i+=1
#     if new == N :
#         print(i)
#         break
#     else:
#         N = new