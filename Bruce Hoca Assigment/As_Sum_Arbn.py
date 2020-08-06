
def my_sum(*x):
    total = 0
    for i in x:
        total += i
    return total




print(my_sum(9, 1, 3, 0, -1))
print(my_sum(5, 7, 4))
print(my_sum(10, -20, 30, 40))