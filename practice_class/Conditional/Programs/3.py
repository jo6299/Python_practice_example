# Write a program input any number and check it is positive or negative or 0
a = int(input("Enter a number: "))
if(a<0):
    print("a is -ve")
elif(a>0):
    print("a is +ve")
else:
    print("a is Zero")