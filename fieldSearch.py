import itertools

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def distance(self, p2):
		return ((self.x-p2.x)**2 + (self.y-p2.y)**2)

	def __hash__(self):
		return hash((self.x, self.y))

	def __eq__(self, other):
		return (self.x, self.y) == (other.x, other.y)

	def __str__(self):
		return str(self.x)+" "+str(self.y)

def main():
	n = 5
	# if not all(n % i for i in xrange(2, n)):
	# 	n+=1
	# 	continue
	allpoints = {Point(x,y) for x in range(n) for y in range(n)}
	for k in range(n**2):
		if k < 10:
			continue
		for E in itertools.combinations(allpoints,k):
			distance_set = {p1.distance(p2)%n for p1 in E for p2 in E}
			if any(not x in distance_set for x in range(n)):
				print "\n".join([" ".join(["X" if Point(r,c) in E else "-" for r in range(n)]) for c in range(n)])
				print [x for x in range(n) if not x in distance_set]
				# break
				print

if __name__ == "__main__":
	main()