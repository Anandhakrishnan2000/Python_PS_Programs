names = ("Navin","Kiran","Harsh","Anandhu")
comp = ("Dell","HP","Apple","Asus")

zipped = dict(zip(names,comp))

print(zipped)

zipp = zip(names,comp)
for (a,b) in zipp:
    print(a,b)


