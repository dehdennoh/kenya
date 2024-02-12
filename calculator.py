firstnumber = float(input("Enter number :"))
lastnumber = float(input("Enter number :"))

operator = input("Enter operator :")

if operator == "+":
    print(firstnumber + lastnumber)
elif operator == "-":
    print(firstnumber - lastnumber)
elif operator == "*":
    print(firstnumber * lastnumber)
elif operator == "/":
    print(firstnumber / lastnumber)
else:
     print("invalid operator")