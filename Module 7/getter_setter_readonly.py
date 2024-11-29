class User:
    def __init__(self,name,age,money) -> None:
        self._name = name
        self._age = age
        self.__money = money
        
    # getter without any setter is read only attribute
    @property
    def age(self):
        return self._age
    
    @property
    def salary(self):
        return self.__money
    
    @salary.setter
    def salary(self,value):
        if value < 0:
            return 'Salary can not be negative'
        else:
            self.__money += value
    
rakib = User('Rakib',21,12000)
# print(rakib.age())
print(rakib.age)
#print(rakib.__money)
print(rakib.salary)
rakib.salary = 4500
print(rakib.salary)
