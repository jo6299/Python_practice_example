# Write a program input acno , name, current balance, transaction amount, transaction code(d/w) 
# calculate net balance.
acno = int(input("Enter acno number: "))
Name = input("Enter Name: ")
current_balance = float(input("Enter Current Balance: "))
transaction_amount = int(input("Enter transaction Amount: "))
transaction_code = (input("Enter transaction Code d/w: "))
if transaction_code == "d":
    net_balance = current_balance + transaction_amount
    print(f"Your Net Balance is: {net_balance}")
elif transaction_code == "w":
    net_balance = current_balance - transaction_amount
    print(f"Your Net Balance is: {net_balance}")
else:
    print("Thank You")
