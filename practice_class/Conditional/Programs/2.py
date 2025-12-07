# Write a program input three numbers and find out the biggest number.

a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = int(input("Enter 3rd Number: "))
if(a>b and a>c):
    print("A is Big Number")
    print(f"The Biggest Number is: {a}")
elif(a<b and c<b):
    print("B is Big Number")
    print(f"The Biggest Number is: {b}")
elif(a<c and b<c):
    print("C is Big Number")
    print(f"THe Biggest Number is: {c}")

else:
    print("Three  Numbers are equal")