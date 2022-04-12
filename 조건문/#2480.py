a,b,c = map(int,input().split())


if (a == b  == c) :
    result = (1000*a) + 10000
    print(result)

elif (a == b) or (b== c) :
    result = (100*b) + 1000
    print(result)

elif (a == c):
    result = (100*a) + 1000
    print(result)

else :
    result = max(a,b,c)*100
    print(result)