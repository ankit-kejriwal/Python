num1 = float(input("ENter first number"))
num2 = (input("ENter oprtator"))
num3 = float(input("ENter second number"))


if num2 == "+":
    print(num1+num3)
elif num2 == '-':
    print(num1 - num3)
elif num2 == '*':
    print(num1 * num3)
elif num2 == '/':
    print(num1 / num3)
else:
    print("wrong operator")
