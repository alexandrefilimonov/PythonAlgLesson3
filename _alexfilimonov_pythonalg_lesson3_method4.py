from random import *
import decimal
import random
def randchar(a,b) :
    return chr(random.randint(ord(a),ord(b)))

s1 = input("Enter number/symbol for random selection from:")
s2 = input("Enter number/symbol for random selection to:")

bIntNumber=1
bFloatNumber=0
bString=0

i=len(s1)-1
while  (i>=0) :
    d = (s1[i:i+1])
    if (d=='.') :
        bIntNumber=0
        bFloatNumber=1
    elif (not(d>='0' and d<='9') or (d=='-') or (d=='+') or (d=='.')) :
        if (i==0) :
            bIntNumber=0
            bString=1
        break      	
    i-=1

bIntNumber2=1
bFloatNumber2=0
bString2=0

i=len(s2)-1
while  (i>=0) :
    d = (s2[i:i+1])
    if (d=='.') :
        bIntNumber2=0
        bFloatNumber2=1
    elif (not(d>='0' and d<='9') or (d=='-') or (d=='+') or (d=='.')) :
        if (i==0) :
            bIntNumber2=0
            bString2=1
        break      	
    i-=1

if (bIntNumber==1 and bIntNumber2==1) :
    s = randint(int(s1),int(s2))
    print("The random int number is ",s)
elif (bFloatNumber==1 and bFloatNumber2==1) :
    s = float(decimal.Decimal(random.randrange(int(float(s1)),int(float(s2)))))
    print("The random float number is ",s)
elif (bString==1 and bString2==1) :
    s = randchar(s1,s2)
    print("The random symbol is ",s)
else:
    print("Unknown format!")



