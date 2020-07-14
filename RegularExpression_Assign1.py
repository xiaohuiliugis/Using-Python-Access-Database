#here are two versions, 1st is simple, 2nd is list comprehension versionn

# data = open('C:\Xiaohui_Study\Coursera\python\RegularExpression.txt','r')

# mytxt = data.read()

# print (mytxt)

# import re
# result = re.findall("[0-9]+",mytxt.rstrip())
# print (result)

# total =0
# for number in result:
# 	num = int(number)
# 	total += num


# print ('Sum:',total)


data = open('C:\Xiaohui_Study\Coursera\python\RegularExpression.txt','r')

mytxt = data.read()

import re

print (sum([int(number) for number in re.findall("[0-9]+",mytxt.rstrip())]))