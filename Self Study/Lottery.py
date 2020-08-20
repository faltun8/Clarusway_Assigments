#daily-python-challenge
"""QUESTION:
Write a Python code to draw whiteball and Powerball numbers for Powerball lottery game.
5 Whiteball numbers are choosen from 01 to 69 and 1 Powerball number is chosen 1 to 26."""

import random

result = list()
for i in range(6):
    if i < 5:
        number = random.randrange(1, 70)
    else:
        number = random.randrange(1, 27)
    result.append(number)

print(result)



