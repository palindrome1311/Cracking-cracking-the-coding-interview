def multiply(a,b):
    print(a,b)
    smaller = min(a,b)
    bigger = max(a,b)
    if(smaller==0):
        return 0

    if(smaller==1):
        return bigger

    s = smaller//2

    side1 = multiply(s,bigger)
    print(side1)
    if(smaller%2==0):
        return 2*side1
    else:
        return (2*side1) + bigger

a=75
b=10
print(multiply(a,b))