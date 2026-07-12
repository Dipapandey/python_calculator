first_no=  float(input("Enter the First Number: "))
Operator= input("Which operation do you want to do (+ - % * / or // ): ")
second_no= float(input("Enter the Second Number: ")65)

if Operator == "+":
    print(first_no + second_no)
elif Operator == "-":
    print(first_no - second_no)
elif Operator == "*":
    print(first_no * second_no)
elif Operator == "%":
    print(first_no % second_no)
elif Operator == "/":
    print(first_no / second_no)
elif Operator == "//":
    print(first_no // second_no)  
else:
    print("Enter a valid Operator")

print("Thanking for using this calculator")
