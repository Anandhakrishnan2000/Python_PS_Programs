from math import pow

def minbid(nums):
    lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q','R','S','T','U','V','W','X','Y','Z']
    vallst = []
    for x in nums:
        b = base(x,lst)
        val = calcval(x,b,lst)
        vallst.append(val)
    return min(vallst)


def base(x,lst):
    lar = -1
    for i in x:
        b = lst.index(i)
        if b>lar:
            lar=b
    return lar+1

def calcval(x,b,lst):
    powerval = len(x)-1
    val=0
    for i in range(len(x)):
        try:
            val += int(x[i])* pow(b,powerval)
        except:
            val += (lst.index(x[i]))*pow(b,powerval)
        powerval-=1
    return int(val)






nums = [x for x in input().split()]
minval = minbid(nums)
print(minval)
