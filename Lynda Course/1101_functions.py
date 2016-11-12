# variable one and two are optional and default, in absence of parameters in 
# testfunc(42, 10), one and two will be active 

def main():
	testfunc(42, 10)
 
def testfunc(number, one = 1, two = 2):
	print('this is a text function',number, one, two)

main()

#output 42, 10, 2
# None can be assigned and tested after function call

##########################

# This will work

#def testfunc():
#	print('this is a text function')

#testfunc()

##########################





##########################

# No content after testfunc() will cause for no 
# indentation error

def main():
	testfunc()

def testfunc():
	pass

testfunc()

main()

##########################