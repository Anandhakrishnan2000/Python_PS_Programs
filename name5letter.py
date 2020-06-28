lst = []
print("Enter 10 user names")
for i in range(10):
    lst.append(input())

def printname(lst):
    for i in lst:
        if(len(i)>5):
            print(i)

print("The users which has names more than 5 letters are")
printname(lst)
