number = int(input("Enter a number please: "))
if number <0:
    print(f"{number} is not a prime number")
else:

    divisors = [i for i in range(2,number) if number % i == 0] #divisors collects the numbers which divides number evenly
    if divisors != []:
        print(f"{number} is not a prime number")
    else:
        print(f"{number} is a prime number")