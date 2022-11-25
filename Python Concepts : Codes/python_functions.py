# #Functions in Python

# def  welcomeMessage():
#     print("Welcome Akash")
# welcomeMessage()

# def addition(a,b):
#     return a+b
# print(addition(3,8))


# def checkCounter(counter):
#     if (counter <= 10):
#         print('Counter : ', counter)
#         checkCounter(counter+1)
#     else:
#         print('recurrsion Stopped')
# counter=1
# checkCounter(counter)


# def avg_of_two_numbers(a,b):
#     print('First Value: ', a)
#     print('Second Value: ', b)
#     result =(a+b)/2
#     return result

# num1 =  10
# num2 =  15
# print("Average : ", avg_of_two_numbers(num1, num2))


# def calculate_factorial(num):
#     if num == 0 or num ==1 :
#         return 1
#     else:
#         result = 1
#         for num in range(1,num+1):
#             result = result * num
#     return result

# num = 5
# print("Factorial or " , num , " is ", calculate_factorial(num))

# How to return multiple values from a function

def square_cube(num):
    square = num*num
    cube =  num*num*num
    return square,cube
num = 10
square, cube = square_cube(num)
print("Square : ", square)
print("Cube : ", cube)


# How to create optionsal arguments in pYthon function
def multiply(a, b = 3):
    result = a * b
    return result
num1 = 5 
num2 = 10
print(multiply(num1,num2))
print(multiply(num1))

#non key-valued arguments
def example_nonkeyed_args(*argv):
    for param in argv:
        print(param)

example_nonkeyed_args('Hello','Akash',25)

#key-Valued arguments
def example_of_kwargs(**kwargs):
    for key,value in kwargs.items():
        print('Key:',key,'Value :',value)

example_of_kwargs(host = 'localhost', port= 8080 , password = 'xxghf')