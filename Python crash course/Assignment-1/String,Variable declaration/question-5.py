# Write  a  Python program to get  a  single string  from  two given strings, separated by a  space  and swap the  first two characters of  each string. 
x,y=input().split()
print(y.replace(y[len(y)-1],x[len(x)-1]),x.replace(x[len(x)-1],y[len(y)-1]))
