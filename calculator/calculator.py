from art_calc import logo
print(logo)


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def calculator(num1, num2, func):
    return func(num1, num2)


def operator(ope):
    if ope == "+":
        return add
    elif ope == "-":
        return sub
    elif ope == "*":
        return multiply
    elif ope == "/":
        return divide


def operation():
    b = True
    while b:
        print(" +\n -\n *\n / ")
        ope = input("Pick an operation: ")
        if ope != "+" and ope != "-" and ope != "*" and ope != "/":
            print("PLEASE TYPE +, -, *, / ONLY!")
        else:
            b = False
    return ope


def continue_calc(result):
    total = result
    b = True
    while b:
        again = input(
            f"\nType 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ").lower()
        if again != "y" and again != "n":
            print("PLEASE TYPE Y/N ONLY!")
        elif again == "y":
            return True
        else:
            return False


def main(num1):
    a = True
    while a:
        ope = operation()
        while True:
            try:
                num2 = int(input("What's the next number: "))
                break
            except ValueError:
                print("Integer only please.")
        result = calculator(num1, num2, operator(ope))
        print(f"{num1} {ope} {num2} = {result}")
        a = continue_calc(result)
        num1 = result


def start():
    while True:
        try:
            num1 = int(input("\nWhat's the first number: "))
            return num1
            break
        except ValueError:
            print("Integer only please.")


system = True
while system:
    num1 = start()
    main(num1)









