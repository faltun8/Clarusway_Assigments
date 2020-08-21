#daily-python-challenge
"""QUESTION:
Write a Python function to process all mathematical operations in below list."""

operations = ["5 + 6", "2 * 3", "8 / 4", "4 - 5"]

def operate(text):
    args = text.split()
    return (lambda x,opr,y : int(x)+int(y) if opr == "+" else \
            int(x)-int(y) if opr == "-" else int(x)*int(y) if opr == "*" else \
            int(x)/int(y)) (args[0],args[1],args[2])

for i in operations:
    print(f"{i} = {operate(i)}")