# list --> []
# tupple --> ()
# set --> {}

numbers = [12,36,42,78,42,12,98]
print(numbers)
number_set = set(numbers)
print(number_set)
number_set.add(55)
print(number_set)
number_set.remove(12)
print(number_set)

for item in number_set:
    print(item)
if 55 in number_set:
    print("exists")

A = {1,2,3}
B = {1,2,3,4,5,6}
print(A&B)
print(A | B)