#Declare & Assign variables
int_var =  10
float_var = 18.25
string_var = 'Akash'  # or another way is to put it in ""
bool_var = True  # for false you can use False

#Function in python for displaying output
print("Hello World!!!")

print("Value of int_var = ",int_var, "- Result Done!!")
print("Value of float_var = ",float_var, "- Result Done!!")
print("Value of string_var = ",int_var, "- Result Done!!")
print("Value of bool_var = ",int_var, "- Result Done!!")

# How to check type of variable or value ?
print(type(int_var))

# How to do the type casting in python?
int_var = int_var + 10;
casted_int_var = float(int_var)
print("Int to Float type casting for int_var : ", casted_int_var)

casted_float_var  = int(float_var)
print("Float to Int Type Casting for float_var : " , casted_float_var)

numeric_str = "123"
numeric_str = int(numeric_str) + 10
print(numeric_str)

# How to take user inputs in python ?
#  input() function

name = input()
age = input()

print("User name : ", name)
print("Age :", age)

#Input with Custom messgaes
name = input("Enter your name:")
age = int(input("Enter your age :"))

print("User name : ", name)
print("Age :", age)

print("Type of Name",type(name))
print("Type of Age",type(age))