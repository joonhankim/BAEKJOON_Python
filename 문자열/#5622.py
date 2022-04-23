#다이얼 문제

alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0
for unit in alpabet_list :  
    for i in unit:  
        for j in word :  
            if i == j :  
                time += alpabet_list.index(unit) +3  #(3초)
print(time)