#menu-driven
a,b,c= input().split()
a=int(a)
b=int(b)
c=int(c)
if c==1:
	print("The Addition of",a,"and",b,"is :",a+b)
elif c==2:
	print("The Subtraction of",a,"and",b,"is :",a-b)
elif c==3:
	print("The Multiplication of",a,"and",b,"is :",a*b)
else:
	print("The Division of",a,"and",b,"is :",a/b)