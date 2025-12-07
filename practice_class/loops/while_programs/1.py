no = int(input("Enter Any Number: "))
reverse_no = 0
while(no>0):
    r=no%10
    reverse_no=reverse_no*10+r
    no=no//10
print(reverse_no)