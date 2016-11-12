class Duck:

	#construtor
	def __init__(self,counter):
		print('construtor')
		self.co = counter

	def quack(self):
		print('Quack! Quack!', self.co)

	def walk(self):
		print('step1 step2 step3',self.co)

	a = 20

	def sprint(self,speed):
		print(speed)

def main():
	
	donald = Duck(101)
	donald.quack()
	donald.walk()
	print(donald.a)
	donald.sprint(50)

	donald_2 = Duck(44)
	donald_2.quack()
	donald_2.walk()
	print(donald_2.a)
	donald_2.sprint(50)

	print (id(donald.a))
	print (id(donald_2.a))
	
main() 