#def main():
	#print("starting main")
	#for i in inclusive_range(0, 5, 1):
		#print("function called, printing the i ")
		#print(i)
#
#def inclusive_range(start, stop, step):
	#print("in the function after the call")
	#i = start
	#while i <= stop:
		#print("yielding i")
		#yield i
		#print("yielded i, increasing the counter")
		#i+=step
		#print("increased counter")
#
#main()


####################################

#def main():
	#for i in inclusive_range(0, 5, 1):
		#print(i)
#
#def inclusive_range(start, stop, step):
	#i = start
	#while i <= stop:
		#yield i
		#i+=step
#
#main()

####################################


def main():
	for i in inc_range(2):
		print(i)


def inc_range(*args):
	lenargs = len(args)
	if lenargs < 1:
		raise TypeError('no argument provided')
		print("atleast one args is expected")
	elif lenargs == 1:
		stop = args[0]
		start = 0
		step = 1
	elif lenargs == 2:
		(start, stop) = args
		step = 1
	elif lenargs == 3:
		(start, stop, step) = args
	else:
		printttt("too many args")

	i = start
	while i <= stop:
		yield i
		i += step

main()