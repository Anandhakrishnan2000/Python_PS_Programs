from numpy import *

arr = array([1,2,3,4,5])
arr1= array([1,2,3,4,5])
arr2= array([7,8,9,10,11])


print(arr)

for i in range(len(arr)):
    arr[i]+=5

print(arr)

arr = arr + 5
print(arr)

arr3 = arr1 +arr2

print(arr3)


print(sqrt(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))
print(concatenate([arr1,arr2]))

arr4 = arr1
print(arr4)
print(arr1)
print(id(arr1))
print(id(arr4))

arr5 = arr1.view() #shallow copy(if any change in one array will reflect in bot arrays)
print(arr5)
print(arr1)
arr5[1]=10
print(arr5)
print(arr1)
print(id(arr1))
print(id(arr5))

arr6 = arr1.copy()#deep copy (change does  not affect the other array)
print(arr6)
print(arr1)
arr6[1]=20
print(arr6)
print(arr1)
print(id(arr1))
print(id(arr1))








