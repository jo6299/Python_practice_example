# W.A.P to print 1 to n Odd Numbers

n = int(input("Enter Any Number: "))
for j in range(1,n):
    if(j%3==0):
        print(j,end=" ")