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


#print instnave variable of a class
print(emp1.company)
print(emp2.company)


#Lets access class varibles from instnace itself
print(emp1.empCount)
print(emp2.empCount)

emp1.empCount = 10
emp2.empCount = 20

print(emp1.empCount)
print(emp2.empCount)
print(Employee.empCount)


#Static method in python
#Static method will be tightly coupled to class

class Car:

    def __init__(self, name, color):
        self.car_name = name
        self.car_color = color
    
    def displayCarDetails(self):
        print("Car name is ", self.car_name, "& Car color is ", self.car_color)

    @staticmethod
    def initialMessage():
        print("Its a nice car...!!!!")

Car.initialMessage()
car1 = Car("Audi A7", "Red" )
car2 = Car("Mercedez Benz Q7", "White")
car1.displayCarDetails()
car2.displayCarDetails()


class Calculation:
    @staticmethod
    def addTwoNums(no1,no2):
        print("Sum : ", no1+no2)

Calculation.addTwoNums(20,40)


