while True:
    value1 = input('First value: ')
    oper = input('Operation (+,-,/,x): ').lower()
    value2 = input('Second value: ')

    if value1.isdigit() and value2.isdigit():
        value1 = int(value1)
        value2 = int(value2)

        if oper == 'x':
            print(value1 * value2)
        elif oper == '/':
            print(value1 / value2)
        elif oper == '+':
            print(value1 + value2)
        elif oper == '-':
            print(value1 - value2)
        else:
            print("Please enter only one of these operators -> '+,-,/,x' ")

    else:
        print("Please enter only numeric values")