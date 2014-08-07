def prime_numbers(n, primes=[], nonprimes=[1], p=2):
	if p not in nonprimes:
		for i in range(p+1, n+1):
			if (i % p == 0 and i not in nonprimes):
				nonprimes.append(i)
		primes.append(p)
	p += 1
	if p > n:
		return primes
	return prime_numbers(n=n, primes=primes, nonprimes=nonprimes, p=p)

print prime_numbers(121)