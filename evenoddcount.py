lst = []
size = int(input("Enter the number of values:"))
print("Enter the values ")
for i in range(size):
    lst.append(int(input()))


def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


even, odd = count(lst)
print("Even : {} Odd : {}".format(even, odd))
