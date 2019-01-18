a=1024211123333
if(a>= -2147483648 and a<= 2147483647):
    print("INT")
elif(a>=9223372036854775808 and a<= 9223372036854775807):
    print("LONG LONG")
else:
    print("LONG")
