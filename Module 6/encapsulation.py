class Bank:
    def __init__(self,holder_name,initial_balance):
        self.holder_name = holder_name      # public
        self._branch = 'Banani'             # protected
        self.__balance = initial_balance    # private
        
    def deposit(self,amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance
    
    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance -= amount
            return amount
        else:
            return 'Not enough money'
    

rakib = Bank('Rakib',10000)
print(rakib.holder_name)
print(rakib.get_balance())
rakib.deposit(40000)
print(rakib.get_balance())
rakib.holder_name = 'Sakib'
print(rakib.holder_name)
print(rakib._Bank__balance)
print(rakib._branch)


