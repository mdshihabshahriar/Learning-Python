class Vehicle:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def __repr__(self) -> str:
        return f'{self.name}, {self.price}'

    def move(self):
        pass

class Bus(Vehicle):
    def __init__(self, name, price,seat):
        self.seat = seat
        super().__init__(name, price)
    def __repr__(self) -> str:
        return super().__repr__()
        
class Truck(Vehicle):
    def __init__(self, name, price,weight):
        self.weight = weight
        super().__init__(name, price)

class PickupTruck(Truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)

class AcBus(Bus):
    def __init__(self, name, price, seat, temparature):
        self.temparature = temparature
        super().__init__(name, price, seat)
    def __repr__(self) -> str:
        print(f'{self.seat}')
        return super().__repr__()
        
green_line = AcBus('Green Line',5000000,28,16)
print(green_line)

    