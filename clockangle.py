
def angle(period,longtitude):
    hnum = (period/360)*longtitude
    hour = int(hnum)
    min = calcmin(hnum)
    angle = calcangle(hour,min)
    return format(angle,'.2f')

def calcmin(hnum):
    n = hnum - int(hnum)
    if n==0:
        min = 0
    else:
        divisor = 1/n
        min = 60/divisor
    return min

def calcangle(hour,min):
    minangle = 6*min
    hourangle = 30*hour
    if minangle==0 and hourangle==360:
        return 0.00
    else:
        extrahrangle = (min/60)*30
        hourangle+=extrahrangle
        angle = hourangle-minangle
    return abs(angle)



period = int(input())
longtitude = float(input())
longtitude = round(longtitude,2)
ang = angle(period,longtitude)
print(ang)