# def sum(num1,num2,num3 = 0) :
#     result = num1+num2+num3
#     return result
# total = sum(89,11,10)
# print(total)

# args

# def all_sum(*numbers):
#     print(numbers)
#     sum = 0
#     for num in numbers:
#         print(num)
#         sum+=num
#     return sum   

# total = all_sum(10,20,30,40,50)
# print("All sum :",total)

def all_sum(num1,num2,*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum+=num
    return sum   

total = all_sum(10,20,30,40,50)
print("All sum :",total)


