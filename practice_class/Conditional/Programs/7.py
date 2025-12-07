# Write a program input cno, cname, srno, erno, slab type(i/c/r) calculate units consumed.
# Conditions: If slab type is industry then unit rate is 5/-
# If slab type is commercial then unit rate is 4/-
# If slab type is residence then unit rate is 3/-
# Calculate total bill.

cno = int(input("Enter your customer No: "))
cname = input("Enter your customer Name: ")
srno = float(input("Enter your starting reading: "))
erno = float(input("Enter your ending reading: "))
slab_type = input("Enter your slab type(i/c/r): ")

units_consumed = erno - srno

if slab_type == "i":
    total_bill = 5 * units_consumed
    print(f"Your total bill is: {total_bill}")
elif slab_type == "c":
    total_bill = 4 * units_consumed
    print(f"Your total bill is: {total_bill}")
elif slab_type == "r":
    total_bill = 3 * units_consumed
    print(f"Your total bill is: {total_bill}")
else:
    print("Error")
    
    