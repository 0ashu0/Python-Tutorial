#python doesnt have switch or case


def main():
	choices = dict(
		one = 'first',
		two = 'second',
		three = 'third',
		four = 'fourth',
		five = 'fifth'
		)

	v = 'one'
	print(choices[v])

	v = 'three'
	print(choices[v])

	#error handling or get method
	v = 'seven'
	print(choices.get(v, 'not present in the dict'))

main()