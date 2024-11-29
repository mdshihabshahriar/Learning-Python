n = int(input()) 
x = []  #empty list
values = input().split()  
for i in values:
    x.append(int(i))  # sob string ke number kore list e jog kora

cnt = 0 
while True:
    even = True

    for num in x:
        if num % 2 != 0: 
            even = False 
            break  
    if not even: 
        break 
    for i in range(n):
        x[i] //= 2 

    cnt += 1  
print(cnt)
