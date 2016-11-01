#tuple is immutable object
#cant insert change or delete things
#faster than lists

#lists are mutable

def main():
	x = (1,2,3)
	print(type(x), x)

	x = [1,2,3]
	print(type(x), x)
	x.append(5)
	print(type(x), x)
	x.insert(0, 7)
	print(type(x), x)

	x = 'string'
	print(type(x), x[2])

	x = 'string'
	print(type(x), x[2:5])	

	x = (1,2,3)
	for i in x:
		print(i)

	x = 'strings'
	for i in x:
		print(i)

main()