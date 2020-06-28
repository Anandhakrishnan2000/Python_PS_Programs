def zero(val=0):
    if type(val) is str:
        op = val[0]
        res = operte(0, op, int(val[1]))
        return res
    else:
        return val


def one(val=1):
    if type(val) is str:
        op = val[0]
        res = operte(1, op, int(val[1]))
        return res
    else:
        return val


def two(val=2):  # your code here
    if type(val) is str:
        op = val[0]
        res = operte(2, op, int(val[1]))
        return res
    else:
        return val


def three(val=3):
    if type(val) is str:
        op = val[0]
        res = operte(3, op, int(val[1]))
        return res
    else:
        return val  # your code here


def four(val=4):  # your code here
    if type(val) is str:
        op = val[0]
        res = operte(4, op, int(val[1]))
        return res
    else:
        return val


def five(val=5):  # your code here
    if type(val) is str:
        op = val[0]
        res = operte(5, op, int(val[1]))
        return res
    else:
        return val


def six(val=6):  # your code here
    if type(val) is str:
        op = val[0]
        res = operte(6, op, int(val[1]))
        return res
    else:
        return val


def seven(val=7):  # your code here
    if type(val) is str:
        op = val[0]
        res = operte(7, op, int(val[1]))
        return res
    else:
        return val


def eight(val=8):  # your code here
    if type(val) is str:
        op = val[0]
        res = operte(8, op, int(val[1]))
        return res
    else:
        return val


def nine(val=9):  # your code here
    if type(val) is str:
        op = val[0]
        res = operte(9, op, int(val[1]))
        return res
    else:
        return val


def plus(val):
    op = "+" + str(val)
    return op


def minus(val):
    op = "-" + str(val)
    return op


def times(val):
    op = "*" + str(val)
    return op


def divided_by(val):
    op = "/" + str(val)
    return op


def operte(val1, op, val2):
    if op == "+":
        return val1 + val2
    if op == "-":
        return val1 - val2
    if op == "*":
        return val1 * val2
    if op == "/":
        return val1 // val2

print(seven(times(five())))

