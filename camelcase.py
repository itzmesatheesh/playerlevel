str1 ="aab"
str2 ="xxy"
for i in range(len(str1)):
    if(i==0):
        str2 +=str1[i].upper()
    elif(str1[i-1].isspace()):
        str2 +=str1[i].upper()
    else:
        str2 +=str1[i]
print(str2)
