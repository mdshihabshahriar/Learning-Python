class Shopping:
    cart = []   # class attributes / static attributes
    origin = 'China'
    
    def __init__(self,name,location):
        self.name = 'Jamuna'
        self.location = 'Dhaka'
        
    def purchase(self,item,price,amount):
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')
    
    @staticmethod    
    def multiply(a,b):
        result = a*b
        print(result)
    
    @classmethod    
    def nothing(self,item):
        print('Nothing to buy',item)
        
bashundhara = Shopping('Bashundhara','Dhaka')
bashundhara.purchase('Dress',500,1000)
bashundhara.nothing('Dress')
Shopping.nothing('Dress')
bashundhara.multiply(6,4)
        