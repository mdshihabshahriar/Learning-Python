n = input()
s = n[::-1]
i = 0
while i < len(s) and s[i] == '0':
    i += 1
print(s[i:])

if n == s:
    print("YES")
else:
    print("NO")
