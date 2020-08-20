#daily-python-challenge
"""QUESTION:
Write a Python code to display multiplication table of numbers 1 to 10 in columns.
Ask user the column number that he/she wants.
For example if user wants 4 columns output of your code should like this."""

def printing_func(starting, ending):
    for i in range(1,11):
        for j in range(starting,ending+1):
            if j * i < 10:
                if i < 10:
                    print(f"{j} x  {i} =  {i * j}", end="   ")
                else:
                    print(f"{j} x {i} =  {i * j}", end="   ")
            else:
                if i < 10:
                    print(f"{j} x  {i} = {i * j}", end="   ")
                else:
                    print(f"{j} x {i} = {i * j}", end="   ")
        print()
    print()


def column_multi(value):
    adder = value
    x = 1
    while True:
        if value < 10:
            printing_func(x, value)
            x = value + 1
            value = value + adder
        else:
            printing_func(x, 10)
            break

column_multi(int(input("How many columns do you wish: ")))