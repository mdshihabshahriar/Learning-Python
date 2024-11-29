def double_decker():
    print('Starting the double decker')
    def inner_fun():
        print('Inside the inner')
        return 3000
    return inner_fun

#print(double_decker())
#print(double_decker()())

def do_something(work):
    print('Work started')
    #print(work)
    work()
    print('Work ended')
    
#do_something(2)
#do_something('Busy')

def coding():
    print('Coding in python')
    
#do_something(coding)

def sleep():
    print('Sleeping and dreaming in python')
    
do_something(sleep)
