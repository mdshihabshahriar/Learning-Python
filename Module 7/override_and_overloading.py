class Person:
    def __init__(self,name,height,weight,age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
    def eat():
        print('Rice')
    
    
class Cricketer(Person):
    def __init__(self, name, height, weight, age,team):
        self.team = team
        super().__init__(name, height, weight, age)
    
    # override
    def eat(self):
        print('Vegetables')
    
    def __add__(self,other):
        return self.age + other.age
    def __len__(self):
        return self.height
    def __gt__(self,other):
        return self.age > other.age

rakib = Cricketer('Rakib',91,70,30,'BD')
akib = Cricketer('Akib',65,72,28,'BD')

print(rakib.name)
print(akib.team)
rakib.eat()
print(rakib + akib)
print(len(rakib))
print(rakib > akib)