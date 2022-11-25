#How to create lamda functions
#First normal function to add integer 5 i  given number
def addFive(no):
    return no+5

x = 7
print(addFive(x))

#Lambda
lamdaAddFive = lambda no : no +5
print(lamdaAddFive(12))

#Multiple arguments
lamdaAddition = lambda x,y : x + y
print(lamdaAddition(9,88))

#Conditional in Lambda
lambdaMax = lambda x,y : x if x > y else y
print(lambdaMax(78,89))

#Lambda fn to concatentae two strings
stringConcat = lambda x,y : x + " " + y
print(stringConcat('Akash','Ghadge')) 

# Map Function
lst = [1,2,3,4,5,6,7,8,9]

squareNum = lambda x : x * x
square_list = list(map(squareNum, lst))
print(square_list)


# Add  sequential respective elements in tow given lists
lst1 = [1,2,3,4,5]
lst2 = [1,1,1,1,1]
addList = lambda x,y : x+y
resultList = list(map(addList, lst1, lst2))
print(resultList)

# Reduce Function
import functools
lstNew = [1,2,3,4,5,6]
result = 0 
addNo = lambda x,y : x + y
result = functools.reduce(addNo,lstNew)
print(result)

# How to use filter
seq = [1,2,3,5,6,7,8,9,10,13]
filterExpression = lambda x : x % 2 == 0
result = list(filter(filterExpression, seq))
print(result)