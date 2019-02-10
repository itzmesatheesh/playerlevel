def playset_53():
	a=input()
	a+='\0'
	b=0
	c=0
	while(True):
		if a[c]=='\0':
			break
		b+=1
		c+=1
	print(b)
playset_53()
