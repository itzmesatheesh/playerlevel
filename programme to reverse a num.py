a=423
rev = 0
while(a>=1):
    rem = a%10
    rev = (rev*10)+rem
    a = a//10
print(rev)
