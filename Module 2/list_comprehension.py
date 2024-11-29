numbers = [25,23,13,35,67,75,10,22,12]
odds = []

for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)
print(odds)