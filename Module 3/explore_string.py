name = 'Shihab\'s Shahriar' # escape
name2 = "Shihab Shahriar"
name3 = """
        Shihab
        Shahriar
"""

print(name3)

for char in name2:
    print(char)
print(name2[2])
print(name2[0:6])
print(name2[-8:])
print(name2[::-1])

if "Shihab" in name2 :
    print("Exists")
print(name2.upper())