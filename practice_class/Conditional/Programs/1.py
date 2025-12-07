#Write a program input two numbers and find out the biggest number.

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
if(a>b):
    print("A is Big Number")
    print(f"The Biggest Number is: {a}")
elif(a<b):
    print("B is Big Number")
    print(f"The Biggest Number is: {b}")
else:
    print("Both Numbers are equal")
