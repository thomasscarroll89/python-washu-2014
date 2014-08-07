def Euclid_algorithm(number1, number2):
	smaller = min(number1, number2)
	larger = max(number1, number2)
	if (larger - smaller) != smaller:
		return Euclid_algorithm(smaller, (larger-smaller))
	elif (larger-smaller) == smaller:
		print smaller
		return smaller

Euclid_algorithm(15, 27)
Euclid_algorithm(100, 1000)
Euclid_algorithm(26, 39)
Euclid_algorithm(35, 3)