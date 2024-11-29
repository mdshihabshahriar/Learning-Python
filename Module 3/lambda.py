# def doubled(x):
#     return x*2

doubled = lambda num : num * 2
square = lambda num : num * num
result = doubled(44)
output = square(9)
print(result,output)

add = lambda x,y : x+y
sum = add(11,33)
# print(sum)

numbers = [12,36,42,78,42,12,98]
# doubled_num = map(doubled,numbers)
doubled_num = map(lambda x:x*2, numbers)
squared_num = map(lambda x:x*x, numbers)
print(numbers)
print(list(doubled_num))
print(list(squared_num))



actors = [
    {'name' : 'Shahrukh', 'age' : 57},
    {'name' : 'Salman', 'age' : 60},
    {'name' : 'Siam', 'age' : 30},
    {'name' : 'Shuvo', 'age' : 35},
]

juniors = filter(lambda actor : actor['age'] < 40, actors)
fivers = filter(lambda actor : actor['age'] % 5 == 0, actors)
print(list(juniors))
print(list(fivers))
