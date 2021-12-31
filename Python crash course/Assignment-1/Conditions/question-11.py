# find out largest number
x,y,z= input("Enter three number : ").split()
x=int(x)
y=int(y)
z=int(z)
print("1st Number =",x,",  2nd Number =",y,", 3rd Number =",y)
if x>y and x>z:
	print("The 3rd Number is the greatest among three.")
elif y>x and y>z:
	print("The 2nd Number is the greatest among three.")
else:
	print("The 3rd Number is the greatest among three. ")