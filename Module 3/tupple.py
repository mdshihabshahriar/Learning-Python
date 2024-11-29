def multiple():
    return 3,4
print(multiple())

things = 'pen','water','laptop','charger','phone'
print(type(things))
print(things)
print(things[0])
print(things[-2])
print(things[1:3])
if 'phone' in things:
    print('exists')
for item in things:
    print(item)
print(len(things))

mega = ([1,2,3],[4,5,6])
print(type(mega))
print(mega[0])
mega[0][1] = 666
print(mega)