#efficient

def main():
	try:
		fh = open('xlines.txt')
	except:
		print("file not found")
	else:	
		for line in fh:
			print(line.strip())

main()





#inefficient

def main():
	try:
		fh = open('xlines.txt')
		for line in fh:
			print(line.strip())
	except:
		print("file not found")

main()