from array import *

a = 5
b = 6

a=a+b
b=a-b
a=a-b


print("The value of a is: ")
print(a)
print("The value of b is ")
print(b)

x= int(input("Enter the first number"))
y= int(input("Enter the second number"))
s = x+y
print("The sum is" ,s)

result = eval(input("Enter an expression"))
print(result)
if result%2 == 0:
	print("The result is even")
else:
	print("The result is odd")



while a<=10:
	print(a)
	a=a+1
print("\n")
for i in range(1,10):
	print(i)

z = 'ANANDHAKRISHNAN'
for i in z:
	print(i)
l = [23,45,67,89]
for i in l:
	print(i)


vals = array('i',[12,34,-5])
print(vals)

newArr = array(vals.typecode, (a for a in vals))