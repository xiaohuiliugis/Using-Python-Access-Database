
fname = 'C:\\Xiaohui_Study\\Coursera\\python\\RegularExpression.txt'

data = open(fname,'r')

for line in data:
	print (line.split()[0])