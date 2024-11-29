# with open('message.txt', 'w') as file: # write kore
#     file.write('I love you, Python!')
    
# with open('message.txt', 'a') as file: # append mane jog kore
#     file.write('I love you, Python!')
    
with open('message.txt', 'r') as file:  # read kore
    text = file.read()
    print(text)
    