#How to use if_else in python

x = 10
y = 5
if(x == y):
    print("X is equal to Y")
else:
    print("X is not equal to Y")


marks = 70
if(marks >= 90):
    print("Grade : A+")
elif (marks >= 80 and marks < 90):
    print("Grade : A")
elif (marks >= 70 and marks < 80):
    print("Grade : B+")
elif (marks >= 60 and marks <70):
    print("Grade : B")
else:
    print("Grade : C")
