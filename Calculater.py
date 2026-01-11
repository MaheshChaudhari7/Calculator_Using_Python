
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

print("what operation do you want to perform\n. + for addition\n, - for substaction\n, * for multiplication\n and / for division:")

operator = input("Enter the operator:")

match operator:
    case '+':
        print(f"the result is: {a + b}")

    case '-':
        print(f"the result is: {a - b}")

    case '*':
        print(f"the result is: {a * b}")

    case '/':
        print(f"the result is: {a / b}")

    case default:
        print(f"there was an error")

