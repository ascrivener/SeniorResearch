n = 5
import math
while (n < 10000):
	if not all(n % i for i in xrange(2, n)):
		n+=1
		continue
	print "N",n
	print min(sum(math.sqrt(D+k*n).is_integer() for k in range(2*n)) for D in range(n))
	# for D in range(n):
	# 	print "D",D
	# 	print sum(math.sqrt(D+k*n).is_integer() for k in range(2*n))
		# for k in range(2*n):
		# 	print math.sqrt(D+k*n)
		# 	print math.sqrt(D+k*n).is_integer()
	n+=1