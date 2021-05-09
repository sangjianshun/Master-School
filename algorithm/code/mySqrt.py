def mySqrt(number,r=0.001):
    x0 = number
    x1 = x0/2 + number/(2*x0)
    while abs(x1-x0) > r:
        x0 = x1
        x1 = x0/2 + number/(2*x0)
    return x1
