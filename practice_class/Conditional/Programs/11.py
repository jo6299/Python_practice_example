# Write a script to check whether the given character is lowercase or uppercase?

# 65 to 90 capital alphabets

# 97 to 122 small alphabets

a = ord(input("Enter a character: "))
if a>=65 and a<=90:
    print("The character is upper case")
elif a>=97 and a<=122:
    print("The character is lower case")
else:
    print("Enter only one character")


