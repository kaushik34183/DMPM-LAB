a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=input("enter operator(+,-,*,/):")
if(c=="+"):
    print("addition:",a+b)
elif(c=="-"):
    print("subtraction:",a-b)
elif(c=="*"):
    print("multiplication:",a*b)
elif(c=="/"):
    print("division:",a/b)
elif(c=="**"):
    print("power:",a**b)
else:
    print("invalid operator")