# strings are immutable object

def main():
	s = "this is string"
	print(s)

	s = "this is \nstring"
	print(s)

	# raw string, used in regular expressions
	s = r"this is \nstring"
	print(s)

	n = 42
	s = "this is {} string".format(n)
	print(s)

	n = 42
	s = r"this is {} \nstring".format(n)
	print(s)

	# tripple quotes
	s = ''' this is string '''
	print(s)

	# tripple quotes
	s = """ this is string """
	print(s)

	# tripple quotes
	# backslash will remove line break
	s = '''\
	this is string
	with multiple lines in it '''
	print(s)

main()