import math
import csv

def CalPois(av, n):
	try:
		return float(math.exp(-av) * math.pow(av, n) / fact(n))
	except:
		pass

def fact(n):
	if n == 0:return 1
	return n * fact(n-1)

if __name__ == '__main__':
	f = open('data.csv', 'w')
	writer = csv.writer(f, lineterminator='\n')
	listdata = []
	av = 5.0
	for n in xrange(0,1000):
		pois = CalPois(av, n)
		listdata.append(pois)
	writer.writerow(listdata)
	