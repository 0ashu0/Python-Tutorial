#def main():
	#num = 1
	#print("main begins")
	#for line in readfile('lines.txt'):
		#print('printing {} line'.format(num))
		#print(line.strip())
		#num = num + 1
#
#
#def readfile(filename):
	#fh = open(filename)
	#return fh.readlines()
#
#main()



def main():
	try:
		for line in readfile('lines.txt'):
			print(line.strip())
	except IOError as e:
		print('can not read the file: ', e)
	except ValueError as e:
		print('wrong filename: ', e)


def readfile(filename):
	if filename.endswith('.txt'):
		fh = open(filename)
		return fh.readlines()
	else:
		raise ValueError('Filename must end with .txt')

main()