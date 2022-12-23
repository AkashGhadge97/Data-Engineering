#How to create a class in Python

class Employee:
    #Class variable - Global variable
    company = 'Brillio'
    empCount=0
    #Constructor
    def __init__(self,name,salary):
        #Instance variables
        #Slef keyword is a pointer to he current object
        self.name = name
        self.salary = salary
        Employee.empCount+=1

    #Method   
    def displayEmployeeInfo(self):
        print("\nEmplyee Name: ",self.name)
        print("Employee Salary: ",self.salary,"\n")

    def displayEmployeeCount(self):
        print("Total Employee Count : ", Employee.empCount)

#Emp1 and Emp2 are the objects of a class
emp1 = Employee('Akash',20000)

print(emp1.displayEmployeeCount())

emp2 = Employee('Tejas', 25000)

emp1.displayEmployeeInfo()

emp2.displayEmployeeInfo()

print(emp2.displayEmployeeCount())

print(emp1.company)
print(emp2.company)


#Difference between class variable and instance variable

