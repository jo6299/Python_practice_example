# Program to check whether a number is divisible by 5 and 11 or not
x = int(input("Enter a Number: "))
if(x%5==0):
    print("X is Divisible by 5")
elif(x%11==0):
    print("X is Divisible by 11")
else:
    print("X is NOT divisible by 5 and 11")
