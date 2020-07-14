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
        elif int(num) > largest:
            largest = int(num)
        elif int(num) < smallest:
            smallest = int(num)
                  
    except:
        print ('Invalid input')
        continue


print("Maximum is ", largest)
print ("Minimum is ",smallest)
