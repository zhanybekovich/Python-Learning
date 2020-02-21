# Calculating Sum or Subtraction

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
operator = input("Choose '+' or '-': ")

if operator == "+":
    print("The sum of two numbers is", num1 + num2)

elif operator == "-":
    print("The difference of two numbers is", num1 - num2)

else:
    print(f"I don't know this {operator}")