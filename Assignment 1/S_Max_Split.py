def maxSplit(s):
    cnt = 0
    result = []
    tmp = ""
    for char in s:
        tmp += char
        if tmp.count("L") == tmp.count("R"):
            cnt += 1
            result.append(tmp)
            tmp = ""
    return cnt, result
    
s = input()
cnt, result = maxSplit(s)
print(cnt)
for str in result:
    print(str)



