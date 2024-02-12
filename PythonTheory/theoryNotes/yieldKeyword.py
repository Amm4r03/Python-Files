# generator function to square a number
def squareOfNums(n):
	for i in range(1, n+1):
		yield i**2

# call the generator function defined above
square_gen = squareOfNums(7)

for square in square_gen:
	print(square, end=" ")