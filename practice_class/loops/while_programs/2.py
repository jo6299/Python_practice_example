# Write a Script to sum of even digits in a given number

no = int(input("Enter Any Number: "))
even = 0
while(no>0):
    r=no%10
    if(r%2==0):
        even = even+r
    no=no//10
print(f"Sum of even numbers is: {even}")


