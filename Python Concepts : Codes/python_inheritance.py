#Inheritance in Python

#Base Class : Parent Class
class Person():
    def __init__(self,name):
        self.name = name

    def displayName(self):
        print(self.name)

    def isEmployed(self):
        print(self.name , "is un-employed");

    def welcomeMessage(self):
        print("Welcome ", self.name)

#Derived class : Child Class
class Employee(Person):

    def __init__(self,name, salary, designation):
        self.salary = salary
        self.designation = designation
        #self.__init__(self,name)
        super().__init__(name)

    def isEmployed(self):
        print(self.name , "is Employed");

    def displayEmpInfo(self):
        print("Name :",self.name)
        print("Salary :",self.salary)
        print("Designation :",self.designation)

emp = Person("Akash")
emp.displayName()
emp.isEmployed()

emp1 = Employee("Tejas",25000,"SDE-1")
emp1.displayName()
emp1.welcomeMessage()
emp1.isEmployed()
print(emp1.name)
emp1.displayEmpInfo()