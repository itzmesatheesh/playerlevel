a=input("")
b=""
for i in range(0,len(a)-1,2):
    b+=a[i+1]
    b+=a[i]
print(b)
