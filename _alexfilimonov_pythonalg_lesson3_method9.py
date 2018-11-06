n1 = float(input("Enter number #1:"))
n2 = float(input("Enter number #2:"))
n3 = float(input("Enter number #3:"))

if ((n1>n2 and n2>n3) or (n3>n2 and n2>n1) or (n1<n2 and n2<n3) or (n3<n2 and n2<n1)) :
    print("The middle number is ", n2)
elif ((n2>n1 and n1>n3) or (n3>n1 and n1>n2) or (n2<n1 and n1<n3) or (n3<n1 and n1<n2)) :
    print("The middle number is ", n1)
elif ((n1>n3 and n3>n2) or (n2>n3 and n3>n1) or (n1<n3 and n3<n2) or (n2<n3 and n3<n1)) :
    print("The middle number is ", n3)
else :
    print("There is no middle number!")
