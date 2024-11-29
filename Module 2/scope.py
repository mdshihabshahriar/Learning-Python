# global variable
balance = 3000

def buy_things(item,price):
    # local variable
    # you can access global variable without using the keyword
    dream_car = "BMW"
    # if you want to modify a global variable, you have to use the global keyword
    global balance 
    print(f"previous balance value",balance)
    balance = balance - price
    print(f"Balance after buying{item}",balance)
# print(dream_car)   
buy_things("Sunglass",1000)
print("After buying balance",balance) 