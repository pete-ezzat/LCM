def multiply_numbers(numbers):
	products = 1
	for number in range(0, len(numbers)):
		products *= numbers[number]
		
	return products
	
#.#.#.

def euclidean_gcd(numbers):
	numbers.sort()
	numbers.reverse()
	n1 = numbers[0]

	for number in range(1, len(numbers)):
		n2 = numbers[number]
		r = n1 % n2

		if r == 1:
			n2 = 1
			break

		while r != 0:
			n1 = n2
			n2 = r
			r = n1 % n2

		n1 = n2

	print('GCD: ', n2)
	return n2

#.#.#.

def warning(message):
	print(message, '\n')

#.#.#.

def lcm(numbers):
	gcd = euclidean_gcd(numbers)
	products = multiply_numbers(numbers)
	
	lcm = products / gcd
	
	print('LCM: ', lcm, '\n')
	
#.#.#.

while True:
	numbers = input("Numbers: ")

	# Convert Strings to Ints
	numbers = numbers.split(" ")
	numbers = list(map(int, numbers))

	# LCM(A,B) = A*B / GCD(A,B) -> MAX 2 Numbers:
	if len(numbers) != 2: 
		warning("Must be 2 numbers.")
		continue

	lcm(numbers)
