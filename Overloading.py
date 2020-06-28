
    #Operator overloading

class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m1
        s3 = Student(m1,m2)

        return s3

    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2

        if s1>s2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)


s1 = Student(58,69)
s2 = Student(60,65)

s3 = s1 + s2
print(s3.m1,s3.m2)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

print(s1)



    #Method Overloading
    

class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def sum(self,a=None,b=None,c=None):

        if a!=None and b!=None and c!= None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a


        return s




s1 = student(58,69)

print(s1.sum(5,9,6))
print(s1.sum(2,3))
print(s1.sum(2))
print(s1.sum())

print()

    #Method Overriding

class A:

    def show(self):
        print("in A Show")

class B(A):

    def show(self):
        print("in B Show")


b1 = B()
b1.show()