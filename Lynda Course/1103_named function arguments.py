#Order of the parameters
	#named arguments
	#arbitrary tuple arguments
	#key word arguments

def main():
	#passing named arguments
	testfunc(10,12,13, 46,45,44, one = 1, two = 2, three = 3)

def testfunc(ten, twelve, thirteen, *args, **kwargs):
	print(ten, twelve, thirteen, args, kwargs)
	print()
	print(kwargs['one'], kwargs['two'], kwargs['three'])
	print()

	for k in kwargs:
		print(k, kwargs[k])
		# k in kwargs[k] is 'one', 'two', 'three'

	print()

	for n in args:
		print(n)

main()