def main():
	print("this is main function")
	fu()
	func(-5)
	func(3)
	func(5)
	funck(1)
	funck(3)
	funckers()

def fu():
	for i in range(13):
		print(i, end=' ')
	print()

def func(a):
	for i in range(a, 10):
		print(i, end=' ')
	print()

def funck(b):
	for i in range(b, 10 ,2):
		print(i, end=' ')
	print()

def funckers(a=7):
	for i in range(a, 10):
		print(i, end=' ')
	print()


main()



# The range() function has two sets of parameters, as follows:

# range(stop)

# stop: Number of integers (whole numbers) to generate, starting from zero. eg. range(3) == [0, 1, 2].
# range([start], stop[, step])

# start: Starting number of the sequence.
# stop: Generate numbers up to, but not including this number.
# step: Difference between each number in the sequence.

# range(): by default will start with 0 