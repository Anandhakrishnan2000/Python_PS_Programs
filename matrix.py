from numpy import *

arr1= array([               #2 dimentional array
    [1,2,3,6,2,5],
    [4,5,6,7,9,3]
])

print(arr1)
print(arr1.dtype)       #arraytype
print(arr1.ndim)        #array dimension
print(arr1.shape)       #array dimensions(m*n)
print(arr1.size)        #array size

arr2 = arr1.flatten()   #to convert into single dimension array
print(arr2)

arr3 = arr2.reshape(2,2,3)  #to convert to multidimentional array
print(arr3)

m1= matrix('1 2 3; 4 2 7; 5 3 6')   #for matrix operations
m2= matrix('1 2 9; 4 5 7; 8 3 6')
print(m1)
print(diagonal(m1))
print(m1.min())
print(m1.max())

#matrix addition with numpy
m3 = m1 + m2
print(m3)

#matrix multiplication with numpy
m4= m1 * m2
print(m4)



#matrix multiplication without numpy
A = array([[1,2,3],[4,2,7],[5,3,6]])
B = array([[1,2,9],[4,5,7],[8,3,6]])

m,n=m1.shape
C = array([[0 for x in range(m)] for y in range(n)])

for i in range(m):
    for j in range(n):
        for k in range(m):
            C[i][j] = C[i][j] + A[i][k]*B[k][j]

print(C)





