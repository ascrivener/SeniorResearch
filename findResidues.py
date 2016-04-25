def findLargest(S,L):
	print L
	if len(L) == 0:
		return [L]
	last = L[-1]
	# L_star = findLargest(L[:-1]) #set of largest= 
	out = []
	flag = False
	for L_star in findLargest(S,L[:-1]):
		print "star",L_star
		if len(L_star) == 0 or all(l - last in S for l in L_star):
			out.append(L_star.append(last))
			flag = True
		elif not flag:
			out.append(L_star)
	return out

import itertools

n = 23
import math
while (n < 24):
	if not all(n % i for i in xrange(2, n)):
		n+=1
		continue
	print "N",n
	for D in range(n):
		for k in range(n):
			# print "D",D
			a = [0 if y in [x for x in range(n) if any((x**2+y**2)%n == D for y in range(n))]
					else 1 for y in range(n)]
			if any(a[x]==0 for x in range(k)):
				continue
			# print "N",n
			# print "D",D
			print a

			L = [x for x in range(n) if a[x] == 1]
			# print L

			# print set(itertools.combinations(L,2))

			# for r in range(1,n+1):
			# 	hole_list = [lst for lst in set(itertools.combinations(L,r)) if all((x-y)%n in L for x in lst for y in lst)]
			# 	if len(hole_list) == 0:
			# 		print tmp
			# 		# if all(L[1] not in choice for choice in tmp):
			# 		# 	print "AOIEJFOAEIJF"
			# 		# 	print L
			# 		# 	print tmp
			# 		break
			# 	tmp = hole_list

			# break

			# print findLargest([x for x in range(n) if a[x]==1],[x for x in range(n) if a[x]==1])
	n+=1
