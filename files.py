
f = open('Myfile.txt','r')

#print(f.read()) prints the whole file

print(f.readline(),end="")
print(f.readline(),end="")
print(f.readline(10))

f1 = open('write','w')
f1.write("Something")
f1.write(" people ")

#copying full contents of  one file to another

for data in f:
    f1.write(data)


#binary files (eg: image files)

f2 = open('origpic.jpg','rb')

f3 = open('copypic.jpg','wb')

for i in f2:
    f3.write(i)