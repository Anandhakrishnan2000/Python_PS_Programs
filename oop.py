


class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("The config is: ",self.cpu,self.ram)



com1 = Computer('i5',16)
com2 = Computer('Ryzen 3',8)

print(type(com1))

com1.config()
com2.config()

class person:

    def __init__(self):
        self.name='navin'
        self.age=18

    def update(self):
        self.age=22

    def compare(self,p2):
        if(self.age==p2.age):
            return True
        else:
            return False


p1 = person()
p2 = person()



if p1.compare(p2):
    print("The age of both person are same")
else:
    print("The ages are different")


#Types of variables

class car:

    wheels = 4                  #class variable(common to all objects)(static variables)

    def  __init__(self):
        self.mil = 10               #instance variable(different in each object)
        self.comp = "BMW"



c1 = car()
c2 = car()

c1.mil = 8

car.wheels=5

print(c1.comp,c1.mil,c1.wheels)
print(c2.comp,c2.mil,c2.wheels)


#Types of methods

class Student:

    school = 'Telusko'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):                      #instance method
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):   #Accessor method(used for accessing value of an instance variable )
        return self.m1
    def set_m1(self,value): #Mutator method (used for modifying the values)
        self.m1 = value

    @classmethod
    def getSchool(cls):      #class method
        return cls.school

    @staticmethod
    def info():             #static method
        print("This is Student class.. in oop module")


s1 = Student(34,47,32)
s2 = Student(89,32,12)

print(s1.avg())
print(s2.avg())
print(Student.getSchool())
Student.info()

    #inner class

class student:          #outer class

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()        #constuctor of inner class

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()             #calling method of inner class from outer class

    class laptop:                   #inner class
        def __init__(self):
            self.brand = 'DELL'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu,self.ram)


s1 = student('Navin',2)
s2 = student('Jenny',3)

s1.show()

lap1 = s1.lap               #creating laptop object
lap2 = s2.lap
print(lap1.brand,lap1.cpu,lap1.ram)

lap3 = student.laptop()
lap3.show()

