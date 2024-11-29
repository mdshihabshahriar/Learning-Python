class Shop:
    shopping_mall = 'Jamuna'
    
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = []      # cart is an instance attribute
        
    def add_to_cart(self,item):
        self.cart.append(item)

sakib = Shop('Sakib')
sakib.add_to_cart('Shoe')
sakib.add_to_cart('Phone')
print(sakib.cart)

rakib = Shop('Rakib')
rakib.add_to_cart('Cap')
rakib.add_to_cart('Sunglass')
print(rakib.cart)