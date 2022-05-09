import sys

def make_table(pattern):
    tmp = [0] * len(pattern)

    j = 0
    for i in range(1,len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = tmp[j-1]
        if pattern[i] == pattern[j]:
            j +=1
            tmp[i] = j
    return tmp

def kmp(string,pattern,table):
    cnt = 0
    pos = []

    j = 0
    for i in range(len(string)):
        while j > 0 and string[i] != pattern[j]:
            j = table[j-1]

        if string[i] == pattern[j]:
            if j == len(pattern)-1:
                cnt +=1
                pos.append(i- len(pattern)+2)
                j = table[j]
            else:
                j += 1
    return cnt,pos

if __name__ == '__main__':
    string = sys.stdin.readline()
    pattern = sys.stdin.readline()

    table = make_table(pattern)

    answer, positions = kmp(string,pattern,table)

    print(answer)
    print(*positions)