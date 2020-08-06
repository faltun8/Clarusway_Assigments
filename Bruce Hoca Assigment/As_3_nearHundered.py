"""assignment-3
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False"""

def near_hundred(value):
    return True if abs(100 - value) <= 10 or abs(200 - value) <= 10 else False





print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))