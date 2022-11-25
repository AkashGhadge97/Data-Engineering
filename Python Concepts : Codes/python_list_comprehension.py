#List Cokprehension
# Write a program to generate a list of 10 numbers
result= []
for i in range(1,11):
    result.append(i)
print(result)

# Now using list comprehension
resultNew = [i for i in range(1,11)]
print(resultNew)

# Get a list of all even numbers between 1 to 50
evenList = [i for i in range(1,50) if i % 2 == 0]
print(evenList)

#Convert all strings into uppercase in given list
listA =  ['hi','hello','bye','nice']
stringUpper = lambda x : upper(x)
resultList = [ x.upper() for x  in listA ]
print(resultList)

#Put all negative numbers after positive numbers from given list
listNew = [1,-1,2,-5,9,10,-6]
resultList = [x for x in listNew if x>0] +  [x for x in listNew if x<0]
print(resultList)