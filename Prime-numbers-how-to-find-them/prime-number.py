def isPrime(num):
    PrimeAnswer = 0

    for e in range(2,num):
        if (num%e) == 0:
            PrimeAnswer = False
            break
        else:
            PrimeAnswer = True

    return PrimeAnswer


for i in range(100):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()