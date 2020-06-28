
def greet():
    print("Hello")
    print("Good morning")

greet()

def add(a,b):
    s = a+b
    return s

s=add(3,4)
print(s)

def add_sub(x,y):
    s = x+y
    d = x-y
    return s,d

su,d=add_sub(6,5)
print(su,d)
print("The sum is",su,"and difference is",d)

# when we use list as arguments it is pass by reference

def person(name,age=18):
    print(name)
    print(age)
    
person('navin',28)              #position argument
person(age=20,name='Anandhu')   #keyword argument
person('Adithya')               #default argument

def sum(*b):                    #variable length
    c = 0
    for i in b:
        c = c+i
    print(c)

sum(1,2,3,4,5)                  #variable length argument

def persondata(name, **data):   #keyword variable length argument
    print(name)
    print(data)
    print(data.items())
    for i,j in data.items():
        print(i,j)


persondata('navin',age=20,city='Kerala',mob=985642312) #keyword variable length argument

a = 10  #global variable
b = 15
def something():
    global b
    b=25
    a=15                #local variable
    x=globals()['a']    #global variable
    print("Inside",a)

something()

print("Outside",a)



#Anonymous function

f = lambda a : a*a

result = f(5)
print(result)



#filter()   used to filter certain values from a list

nums = [3,2,6,8,4,6,2,9]
evens = list(filter(lambda n : n%2==0 ,nums))
print(evens)

#map()  used to map certain values with the elements of the list
doubles = list(map(lambda n: n*2,evens))
print(doubles)

#reduce() used to reduce a list to a single result based upon the function operation
from functools import reduce

sum = reduce(lambda a,b: a+b,doubles)
print(sum)


        #Decorators

def div(a,b):
    print(a/b)


def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div1 = smart_div(div)
div1(2,4)

        #Modules

from factorial import *   #importing created modules
fact(10)

if(__name__=="__main__"): #if we import this module in another python file this code will never work
    print("Hello")



















