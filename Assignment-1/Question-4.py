# exam date
print("Enter your exam date like (dd,mm,yyyy)")
x=input("exam_st_date =")

dd=(x[1]+x[2])
mm=(x[4]+x[5])
yyyy=(x[7]+x[8]+x[9]+x[10])
z="/".join([dd,mm,yyyy])
print("The examination will start from: "+z)