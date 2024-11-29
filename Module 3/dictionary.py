numbers = [12,36,42,78,42,12,98]
person1 = ['Shihab','Dhaka',22,'Student']

person = {'name' : 'Shihab','address' : 'Dhaka','age' : '22','job' : 'Student'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())
person['language'] = 'Python'
person['name'] = 'Shahriar'
del person['age']
print(person)

for key,values in person.items():
    print(key,values)
    