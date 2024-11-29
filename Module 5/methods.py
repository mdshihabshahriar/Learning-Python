def call():
    print('Calling someone i dont know')
    return 'call done'
class Phone:
    Price = 70000
    Brand = 'Iphone'
    Colour = 'Silver'
    features = ['Camera','Speaker','Portrait']
    
    def call(self):
        print('Calling one person')
        
    def send_sms(self,phone,sms):
        text = f'sending sms to {phone} and message: {sms}'
        return text

my_phone = Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(1772773,'I missed to miss you')
print(result)