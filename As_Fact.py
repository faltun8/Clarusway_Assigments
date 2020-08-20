def my_fact(x):
    if x < 2:
        return 1
    return x * my_fact(x - 1)


print(my_fact(5))
print(my_fact(4))
print(my_fact(3))