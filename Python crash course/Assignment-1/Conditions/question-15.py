Roll=int(input("Roll No: "))
Name=input("Name of Student : ")
Physics,Chemistry,ComputerApplication =(input("Input the  marks of  Physics, Chemistry  and Computer  Application :")).split()
print("Marks in Physics :",Physics)
print("Marks in Chemistry :",Chemistry)
print("Marks in Computer Application :",ComputerApplication)
Physics =int(Physics)
Chemistry=int(Chemistry)
ComputerApplication=int(ComputerApplication)
print("Total marks =",(Physics+Chemistry+ComputerApplication))
x=(Physics+Chemistry+ComputerApplication)/3
print("Percentage = %.2f"%x)
if x>=80 and x<=100:
	print("Division = First")
elif x>=60 and x<=79:
	print("Division = Second")
elif x>=30 and x<=59:
	print("Division = Third")
elif x>=0 and x<=29:
	print("Division = Fail")
else:
	print("Error")