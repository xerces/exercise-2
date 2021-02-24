e=0
o=0
for i in range(1,101):
	if(i%2==0):
		e=e+i
	else:
		o=o+i

print("The sum of all evens is {}. And the sum of all odds is {}.".format(e,o))	