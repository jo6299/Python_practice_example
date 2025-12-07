# Write a Script to sum of 5 divisible in a given number
no = int(input("Enter Any Number: "))
divisible_5=0
while(no>0):
    r=no%10
    if(r%5==0):
        divisible_5=divisible_5+r
    no=no//10
print(f"The sum of digits Divisible by 5: {divisible_5}")