
x1 = float(input("Enter x coordinate for the first dot:"))
y1 = float(input("Enter y coordinate for the first dot:"))
x2 = float(input("Enter x coordinate for the second dot:"))
y2 = float(input("Enter y coordinate for the second dot:"))
a = (y2-y1)/(x2-x1)
b = y1 - a * x1

if (b>0) :
    print("Line equation is y=",a,"* x + ",b)
else :
    print("Line equation is y=",a,"* x ",b)

