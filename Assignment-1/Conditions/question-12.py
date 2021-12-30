# check Triangle 
x,y,z=input("Enter three pointer distance : ").split()
x=int(x)
y=int(y)
z=int(z)
if x==y and y==z and z==x:
	print("This is an equilateral triangle.")
elif x!=y and y!=z and z!=x:
	print("This is a scalene triangle.")
else:
	print("This is an isosceles triangle ")