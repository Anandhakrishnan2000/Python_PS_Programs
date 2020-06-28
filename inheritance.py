class A:

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A):             #single level inheritance
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(B):             #multilevel inheritance
    def feature5(self):
        print("Feature 5  working")

class Z:
    def feature0(self):
        print("Feature 0 working")


class D(A,Z):                 #multiple inheritance
    def feature6(self):
        print("Feature 6  working")


a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

c1 = C()

c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()


d1 = D()

d1.feature1()
d1.feature2()
d1.feature6()
d1.feature0()
print()

    # Constructor in python

class E:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class F(E):             #single level inheritance

    def __init__(self):
        super().__init__() #super() is used to accses the methods of super class
        print("in B init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")



f1 = F()























