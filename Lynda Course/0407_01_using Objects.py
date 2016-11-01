#defining class
class Egg:
	#defining constructor
	def __init__(self, kind = "fried"):
		self.kind = kind
		self.kind1 = self.kind.upper()

	def whatKind(self):
		return self.kind1

	#def defineKind(customKind):
	#	return customKind

def main():
	#fried = Egg()
	#scrambled = Egg('scrambled egg')
	#print(scrambled.whatKind())

	#object mydish of class Egg()
	mydish = Egg() #constructor gets executed
	print(mydish.kind)
	print(mydish.kind1)

	myAnotherDish = Egg('Damaged Egg')
	print(myAnotherDish.whatKind())
	
	#mySpecialDish = Egg()
	#print(mySpecialDish.defineKind(self.kind1))


main()

#Question: is it possible to pass constructor variable in Function?