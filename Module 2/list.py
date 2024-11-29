numbers = [10,20,30,40,50,60,70,80,90]
print([numbers[3],numbers[-3]])

# list(start:end) start from the start index and stop before the end index
print(numbers[2:6])

# list(start:end:step)
print(numbers[2:6:1])
print(numbers[2:6:3])
print(numbers[6:2:-2])
print(numbers[2:])
print(numbers[:5])
print(numbers[:])
print(numbers[::-1]) # shortcut reverse 