# Write a program input employee no, employee name, employee salary, designation(m/a/c) .
# If designation is manager then bonus is 20% on his salary
# If designation is analyst then bonus is 10% on his salary
# If designation is clerk then bonus is 5% on his salary, 
# Calculate total salary

employee_no = int(input("Enter your employee number: "))
employee_name = input("Enter your name: ")
employee_salary = float(input("Enter your salary: "))
designation = input("Enter your designation (m/a/c): ")

if designation == "m":
    bonus = 0.20 * employee_salary
    total_salary = bonus + employee_salary
    print(f"Your Total Salary is: {total_salary}")
elif designation == "a":
    bonus = 0.10 * employee_salary 
    total_salary = bonus + employee_salary
    print(f"Your Total Salary is: {total_salary}")
elif designation == "c":
    bonus = 0.05 * employee_salary
    total_salary = bonus + employee_salary
    print(f"Your Total Salary is: {total_salary}")
else:
    print("Bye")
