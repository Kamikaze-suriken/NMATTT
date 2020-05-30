import random 
from random import randrange
def miller_rabin(n, k = 64):
	if n == 2:
		return True
	if not n & 1:
		return False

	def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1:
			return True
		for i in range(s - 1):
			if x == n - 1:
				return True
			x = pow(x, 2, n)
		return x == n - 1

	s = 0
	d = n - 1

	while d % 2 == 0:
		d >>= 1
		s += 1

	for i in range(k):
		a = randrange(2, n - 1)
		if not check(a, s, d, n):
			return False
	return True
def check(n):
    if n > 1e12:
        return miller_rabin(n)
    if n % 2 == 0:
        return False 
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
def generate(n):
    tmp = random.randint(2 ** (n - 1), 2 ** n)
    while True:
        if check(tmp) == True:
            prime_number = tmp
            break 
        else:
            tmp = random.randint(2 ** (n - 1), 2 ** n)
    return prime_number
print(generate(10)*generate(10))
#52593746111299673917462180378616675287554472293960928632820865884284203124461  2788276781 2750610521
#62498583253142607477966477133203944923275932655067879070835857681721169284823
#71182774100717587506080181170062514792176017725614199654354224825944047872889