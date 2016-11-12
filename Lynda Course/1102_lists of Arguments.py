
def main():
	testfunc(1,2,3,43,44,45,46)

def testfunc(this, that, other, *args):
	print(this, that, other, args)
	for n in args:
		print(n, end = ' ')


main()