
# study notes from Python Structure @ Coursera
#

# Dictionary

# counting pattern
counts = dict()
print ('Enter a line of text:')
line = input('')

words = line.split()

print ('Words:' words)
#get method gets the value corresponds to the key (word), if word does not exist, use default 0 
for word in words:
	counts[word] = counts.get(word,0)+ 1
print ('Counts:', counts)



# Retrieving lists of Keys and Values: get a list of keys, values, or items(both) from a dictionary

jj  = {'chunck':1, 'and':42,'jan':100}

#to get a list of the keys
print (list(jj))
#['chunck', 'and', 'jan']
# Another method to get a list of the keys
print (jj.keys())
#dict_keys(['chunck', 'and', 'jan'])
#give a list of the values
print (jj.values())
#dict_values([1, 42, 100])

print (jj.items())
#dict_items([('chunck', 1), ('and', 42), ('jan', 100)])



# Python allows two iteration variables, key-value pairs can both be variables
jj  = {'chunck':1, 'and':42,'jan':100}

for aaa, bbb in jj.items():
	print (aaa + " &",bbb)
# the output is as follows:
# chunck & 1
# and & 42  
# jan & 100


# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = dict()
for line in handle:
    if line.startswith("From") and not line.startswith("From:"):
        #print (line.split()[5].split(":")[0])
        hour_dig = line.split()[5].split(":")[0]
        hours[hour_dig] = hours.get(hour_dig,0)+1
print (hours)
# {'09': 2, '18': 1, '16': 4, '15': 2, '14': 1, '11': 6, '10': 3, '07': 1, '06': 1, '04': 3, '19': 1, '17': 2}
sort = sorted([(k,v) for k,v in hours.items()])

print (sort)
#[('04', 3), ('06', 1), ('07', 1), ('09', 2), ('10', 3), ('11', 6), ('14', 1), ('15', 2), ('16', 4), ('17', 2), ('18', 1), ('19', 1)]
for k,v in sort:
    print (k,v)
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

# study notes from Python for everybody @ Coursera

# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        if largest is None or smallest is None:
            largest = int(num)
            smallest =int(num)
        elif int(num) >largest:
            largest = int(num)
        elif int(num) < smallest:
            smallest = int(num)
    except:
        print ('Invalid input')
        continue

print("Maximum is", largest)
print ("Minimum is",smallest)

# Invalid input
# Maximum is 10
# Minimum is 2