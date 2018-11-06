def equilateral(n1,n2,n3):
    if  (n1 == n2 and n2 == n3 and n1>0 and n2>0 and n3>0) : 
        return 2 #equilateral
    else :
        return -1 #not equilateral

def isosceles(n1,n2):
    if  (n1 == n2) : 
        return 0 #isosceles  
    else :
        return 1 #versatile

n1 = float(input("Length 1:"))
n2 = float(input("Length 2:"))
n3 = float(input("Length 3:"))

if (equilateral(n1,n2,n3)==2) :
    print("This triangle is equilateral!")
elif (n1>=(n2+n3) or n2>=(n1+n3) or n3>=(n2+n1) or n1<=0 or n2<=0 or n3<=0 ) : #triangle is impossible
    print("Triangle is impossible!") 
else :
    if (n1!=n2 and n1!=n3 and n2!=n3) :  
       print("This triangle is versatile!")  
    else : 
       print("This triangle is isosceles!")  
