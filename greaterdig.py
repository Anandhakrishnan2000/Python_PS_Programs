from itertools import permutations

def smallgreater(a,b):
    li = [x for x in str(a)]
    greatlst = []
    perm = permutations(li)
    flag = 0
    for i in perm:
        num = int(('').join(i))
        if num>b:
            greatlst.append(num)
            flag=1
    if flag==0:
        return -1
    else:
        return min(greatlst)

a,b = [int(x) for x in input().split()]
small = smallgreater(a,b)
print(small)


