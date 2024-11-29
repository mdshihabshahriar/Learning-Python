from abc import ABC,abstractmethod
class Animal:
    @abstractmethod
    def eat(self):
        print('I need food')
        
    @abstractmethod
    def move(self):
        pass
    
class Monkey(Animal):
    def __init__(self,name) -> None:
        self.catagory = 'Monkey'
        self.name = name
        super().__init__()
        
    def eat(self):
        print('Eating Banana')
    def move(self):
        print('Hanging on the branches')

a = Monkey('lucky')
a.eat()

