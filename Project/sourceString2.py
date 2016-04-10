def sourceString (input):	
	lines = [line.strip('\n') for line in input]
	s = "".join(lines)
	print s
	
sourceString(open('methods.txt', 'r'))