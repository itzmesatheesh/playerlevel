a=6
s=Sundar
b=""
l=['a','e','i','o','u','A','E','I','O','U']
for i in reversed(s):
    if i not in l:
        b+=i
print(b)
