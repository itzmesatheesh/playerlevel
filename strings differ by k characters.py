a,b,l=map(str,input().split())
l=int(l)
c=0
if(len(a)!=len(b)):
    print("no")
else:
    for i in range(len(a)):
        if a[i]!=b[i]:
            c+=1
if c==l:
    print("yes")
else:
    print("no")
