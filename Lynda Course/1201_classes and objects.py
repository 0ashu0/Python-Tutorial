class Duck:
	def quack(self):
		print('Quack! Quack!')

	def walk(self):
		print('step1 step2 step3')

def main():
	donald = Duck()
	print(donald)
	donald.quack()
	donald.walk()

main() 