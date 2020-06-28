
nums = [7,8,9,5]

it = iter(nums)

print(it.__next__())

print(next(it))

for i in nums:
    print(i)

print()
    #craeting own iterator

class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    def __next__(self):
        if(self.num<=10):
            val = self.num
            self.num+=1

            return val
        else:
            raise StopIteration

values = TopTen()


print(values.__next__())
print(values.__next__())
print(values.__next__())
print()

for i in values:
    print(i)

print()


        #Generator

def topten():

    yield 1         #used for generator object(will not terminate the function but returns the value)
    yield 2
    yield 3
    yield 4
    yield 5




values  = topten()

print(values.__next__())
print(values.__next__())

for i in values:        #will print remaining vlaues
    print(i)

print("--------------------------------------------------")
#perfect square program

def psqten():
    n = 1
    while n<=10:
        sq = n*n
        yield sq
        n+=1

values=psqten()

for i in values:
    print(i)