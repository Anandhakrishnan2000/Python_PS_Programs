

a = 5
b = 2

try:                #tries the statement to be executed
    print(a/b)
except Exception:   #will be executed only when an exception occurs
    print("Hey, You cannot divide a Number by Zero")
print("Bye")


try:
    print("resourse open")
    print(a/b)
    k= int(input("Enter a number"))
    print(k)

except ZeroDivisionError as e:      #can handle zero division eception
    print("Hey, You cannot divide a Number by Zero", e)

except ValueError as e:         #can handle error with different datatype
    print("Invalid input")

except Exception as e:      #can handle all exceptions
    print("Something went wrong")

finally:                #finally block will be executed if we get error as well as if we dont get error
    print("resourse closed")



