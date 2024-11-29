n = input()
for i in n :
    my_list = input()
    i+=i
rev_my_list = int(my_list[::-1])
for i in my_list:
    if rev_my_list[i] > int(my_list[i]):
        my_list1[i] = rev_my_list[i]
        i+=i
print(my_list1)
