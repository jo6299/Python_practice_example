# Write a Script to sum of prime numbers in a given number
no = int(input("Enter any number: "))
prime_no = 0
while(no>0):
    r=no%10
    if (r in [2,3,5,7]):
        prime_no=prime_no+r
    no=no//10
print(f"The sum of the prime numbers: {prime_no}")