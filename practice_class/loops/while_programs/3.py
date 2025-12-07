# Write a Script to sum of odd digits in a given number

no = int(input("Enter Any Number: "))
odd = 0
while(no>0):
    r=no%10
    if(r%2!=0):
        odd = odd+r
    no=no//10
print(f"Sum of even numbers is: {odd}")

