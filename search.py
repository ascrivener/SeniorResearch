def print_2d(arr):
	print('\n\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in arr]))

def test(C,n):
	line_locations = [i for i in range(C)]
	points = [Point(x,y) for x in range(n) for y in line_locations]
	distances = {Point(0,0).distance(p2)%n for p2 in points}
	if len({x for x in range(n)}-distances)==0:
		return False
	return True

def main():	
	n = 18
	while (n < 19):
		n+=1
		if not all(n % i for i in xrange(2, n)):
			continue

		print n
		allPoints = {Point(x,y) for x in range(n) for y in range(n)}
		# points = [['-' for x in range(n)] for x in range(n)]
		# print_2d(points)

		for C in range(n):
			if test(C+1,n):
				continue
			# C=3
			line_locations = [i for i in range(C)]
			while(True):
				# print line_locations
				points = {Point(x,y) for x in range(n) for y in line_locations}
				# distances = {Point(0,line_locations[c1]).distance(Point(x,line_locations[c2]))%n for c1 in range(C) for x in range(n) for c2 in range(c1,C)}
				distances = {p1.distance(p2)%n for p1 in points for p2 in points}
				if len({x for x in range(n)}-distances)!=0:
					print "WOAH"
					print line_locations
					difference = allPoints-points
					for newPoint in difference:
						# print "trying",newPoint
						if len(distances.union({newPoint.distance(p2) for p2 in points})) < n:
							print "OAIJWFOAIJFEJIAOFIJAOEFIJAOIWEFJOAIJ"
							print "C",C
							print "n",n
							print "point", newPoint.x,newPoint.y
						# print line_locations
				# allPoints
				# print points
				
				
				# print distances
				# print line_locations
				# print

				# points = {Point(x,(y+x)%n) for x in range(n) for y in line_locations}
				# distances = {p1.distance(p2)%n for p1 in points for p2 in points}

				# difference = allPoints-points
				# for newPoint in difference:
				# 	# print "trying",newPoint
				# 	if len(distances.union({newPoint.distance(p2) for p2 in points})) < n:
				# 		print "AOSFIJEAOIFJEIJFIEFIJEIJIE"
				# 		print "C",C
				# 		print "n",n
				# 		print "point", newPoint.x,newPoint.y
				# print distances
				# print line_locations

				if line_locations[C-1] < n-1:
					line_locations[C-1]+=1
				else:
					index = C-1
					while index > 0 and line_locations[index] == line_locations[index-1]+1:
						index-=1
					if index == 0:
						break
					else:
						line_locations[index-1]+=1
						while (index < C):
							line_locations[index] = line_locations[index-1]+1
							index+=1
			break



			

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





if __name__ == "__main__":
	main()