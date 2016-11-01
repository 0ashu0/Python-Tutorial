#dictionaries are mutable object

def main():
	d = {'one': 1, 'two':2, 'three': 3, 'four': 4}
	
	print(d)
	print()

	print(d.keys())
	print()

	for k in d:
		print(k, d[k])
	print()

	d = {'one': 1, 'two':2, 'three': 3, 'four': 4}
	for k in sorted(d.keys()):
		print(k, d[k])


	#keyword arguments as alternative
	d = dict(
		one = 1,
		two = 2,
		three = 3,
		five = 5
		)
	print(d)

	d['seven'] = 7

	print(d)


main()