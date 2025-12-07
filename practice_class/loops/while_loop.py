n = 10
sum = 0
while(n>0):
    r=n%10
    n=n//10
    sum=sum+r
print("Sum is:",sum)

print("----------------------")

n = 10
sum = 0
while(n>0):
    r=n%10
    n=n//10
    sum=sum+r**3
print("Sum is:",sum)

print("----------------------")

n = 10
sum = 0
while(n>0):
    r=n%10
    n=n//10
    sum=sum*10+r
print("Sum is:",sum)

print("----------------------")

n = 2
while(n>0):
    print(n,end="\t")
    n-=1
    
print("----------------------")

n = 6
while(n<0):
    print(n,end="\t")
    n-=1
print("Thank You")

print("----------------------")

n = 1
while(n<0):
    print(n)
    n=n-1
print("Thank You")