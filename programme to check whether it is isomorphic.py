a= {}
b=[]
d="yes"
str1,str2 = map(str,input("").split())
if(len(str1)!=len(str2)):
    d="no"
else:
    for i in range(len(str1)):
        if str1[i] in b:
            temp =a[str1[i]]
            if(temp == str2[i]):
                d = "yes"
            else:
                d="no"
        else:
            b.append(str1[i])
            a[str1[i]]=str2[i]
print(d)
