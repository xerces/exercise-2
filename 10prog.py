def reverse_list(l):
	a=[]
	x=len(l)
	for i in range(x-1,-1,-1):
		a.append(l[i])
	return a	

print(reverse_list(["A", "B", "C"]))