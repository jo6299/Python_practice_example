for i in range(1,5,1):
    print(i,end=" ")

print("----------------------")

for i in range(10):
    print(i,end=" ")

print("----------------------")

for i in range(10,1,-1):
    print(i,end=" ")

print("----------------------")

for i in range(4,10,3):
    print(i,end=" ")
    
print("----------------------")

for i in range(10):
    if(i%2!=0):
        print(i,end=" ")

print("----------------------")

sum = 0
for i in range(1,6):
    if(i%2==0):
        sum = sum+1
print(i,end=" ")

print("----------------------")

for i in range(1,6):
    if(i%3==0):
        print(i,end=" ")

print("----------------------")

# n = 10
# count = 0
# for i in range(n):
#     if(n%i==0):
#         count=count+1
# print(count)

print("----------------------")

n=5
a=1
for i in range(1,n+1):
    a=a*i
    print(a,end=" ")

print("----------------------")

x = [2,5,3,6,1,4]
s = 0
for i in x:
    if(i%2==0):
        s=s+i
        print(s,end=" ")

print("----------------------")

x = [2,5,3,6,1,4]
s = 0
for i in x:
    if(i%2!=0):
        s=s+i
        print(s,end=" ")

print("----------------------")

for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")
print()

print("----------------------")

for i in range(1,5):
    for j in range(1,1+i):
        print("*",end=" ")
    print()
    
print("----------------------")

k = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end=" ")
        k+=1
    print()
    
print("----------------------")
