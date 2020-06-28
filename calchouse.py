
def calchouse(i):
    N, B = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    count = 0
    buy = 0
    while(len(A)>=0):
        m =min(A)
        if buy+m <= B:
            buy = buy+m
            count+=1
        else:
            break
        A.pop(A.index(m))
    print("Case #{}: {}".format(i,count))

T = int(input())
for i in range(T):
    calchouse(i + 1)

