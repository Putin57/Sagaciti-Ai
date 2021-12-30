x=input()
if len(x)>=3:
	if x[-3:]=="ing":
		print(x+"ly")
	else:
		print(x+"ing")
else:
	print(x)
	