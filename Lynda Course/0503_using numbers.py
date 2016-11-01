def main():
	number = 42
	print(type(number), number)

	number = 42.0
	print(type(number), number)

	number = 42.0 / 9
	print(type(number), number)

	number = 42 / 9
	print(type(number), number)

	number = 42 // 9
	print(type(number), number)

	number = round(42 / 9)
	print(type(number), number)

	number = round(42 / 9, 2)
	print(type(number), number)

	number = 42 % 9
	print(type(number), number)

	number = int(42)
	print(type(number), number)

	number = float(42)
	print(type(number), number)

if __name__ == "__main__": main()