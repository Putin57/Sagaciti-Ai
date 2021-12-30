letter =input().lower()
dict={}
for x in letter:
	keys=dict.keys()
	if x in keys:
		dict[x]+=1
	else:
		dict[x]=1
print(dict)