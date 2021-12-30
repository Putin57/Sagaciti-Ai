#difference between two date
import datetime 
first=input("Enter 1st date like: yyyy,mm,dd: ")
second=input("Enter 2nd date like : yyyy,mm,dd: ")
first_list=first.split(",")
second_list=second.split(",")
date1=datetime.date(int(first_list[0]),int(first_list[1]),int(first_list[2]))
date2=datetime.date(int(second_list[0]),int(second_list[1]),int(second_list[2]))
if date1>date2:
	difference =(date1-date2).days
else:
	difference =(date2-date1).days
print(difference,"days")
