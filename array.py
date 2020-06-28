from array import *


arr = array('i',[])
n = int(input("Enter the size of the array"))
print("Enter "+ str(n) + " values")
for i in range(n):
	arr.append(int(input()))
print(arr)

item = int(input("Enter the element to be searched"))
for x in range(n):
	if(arr[x]==item):
		print("The element is found at th index " + str(x))
		break
else:
	print("The element is not found")

