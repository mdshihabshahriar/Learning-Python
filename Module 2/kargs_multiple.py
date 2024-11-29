# def full_name(first,last):
#     name = f"Full name is :{first},{last}"
#     return name
# # name = full_name("Shihab","Shahriar")
# name = full_name(last="Shahriar",first="Shihab")
# print(name)

# kargs
# def name(title,first,last,**addition):
#     name = f"{first} {last}"
#     print(addition["title"])
#     for key,value in addition.items():
#         print(key,value)
#     return name
# ans = name(first="Shihab",last="Shahriar",title="MD")
# print(ans)

# return multiple things from an array

# def a_lot(num1,num2):
#     sum = num1 + num2
#     multi = num1*num2
#     remain = num1 - num2
#     # return[sum,multi,remain]
#     return sum,multi,remain

# everything = a_lot(50,2)
# print(everything)



def fun(args,**kwargs):
    for key,value in kwargs.items():
        print(key,"=",value)

fun("MD",first = 'Shihab',last = 'Shahriar')