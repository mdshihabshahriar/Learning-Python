class Phone:
    manufactured = 'China'
    
    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price
        
phone1 = Phone('Tim Cook','Iphone',120000)
print(phone1.owner,phone1.brand,phone1.price)

phone2 = Phone('Lee Jae-yong','Samsung',100000)
print(phone2.owner,phone2.brand,phone2.price)
        