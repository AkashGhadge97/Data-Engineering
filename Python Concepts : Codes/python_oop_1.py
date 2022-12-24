class School:
    studentCount=0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        School.studentCount+=1

    def displayStudent(self):
        print("Name : ",self.name," Age:",self.age)

st1= School("John", 25)
st2 = School("Rock", 24)

st1.displayStudent()
st2.displayStudent()
print("Total Students : ",st1.studentCount)
