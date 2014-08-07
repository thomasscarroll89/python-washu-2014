def sqr(number, guess, precision):
	guess = float(guess)
	number = float(number)
	new_guess = guess - (guess**2 - number)/(2*guess)
	while (abs(new_guess - guess) >= precision):
		guess = new_guess
		new_guess = guess - (guess**2 - number)/(2*guess)
	print "%f" %new_guess

sqr(579, 25, 0.00000000001)