n = int(input("Enter integer number three digits long that is more than 0:"))
s = str(n)
if (len(s)!=3) :
    print("This is not integer number three digits long that is more than 0!",s)
else :
    sum=0 
    multiplication=1
    i=len(s)-1
    while  (i>=0) :
        digit = s[i:i+1]
        print("Digit is ",digit)
        sum+=int(digit)	    		
        multiplication*=int(digit)
        i-=1
    print("Sum of three digits is ",sum)
    print("Multiplication of three digits is ",multiplication)

