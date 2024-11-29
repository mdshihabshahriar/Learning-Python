class Shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []
        
    def add_to_cart(self,item,price,quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)
        
    def checkout(self,amount):
        total = 0
        for item in self.cart:
            print(item)
            total += item['price'] * item['quantity']
        print('Total price',total)
        if total > amount:
            print(f'Please provide {total - amount} more')
        else:
            extra = amount-total
            print(f'Here is your items and extra money: {extra}')
            
sakib = Shopping('Sakib')
sakib.add_to_cart('Egg',12,24)
sakib.add_to_cart('Potato',50,6)
sakib.add_to_cart('Rice',50,5)

#sakib.checkout(600)
sakib.checkout(1500)
            