def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
    
fact(5)

def reccfact(n):
    if(n==0 or n==1):
        return 1
    else:
        f = n * reccfact(n-1)
    return f

print(reccfact(5))

