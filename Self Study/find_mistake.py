"""Rule is :
if number is smaller than 2, multiply number with 10
if number is between 2 and 4, take square of number
if number is greater than 4, add 10 to number."""


df = {"one":[1,2,3,4,5]}
df["two"] = [x*10 if x<2 else x**2 if x<4 else x+10 for x in df["one"]]

print(df)