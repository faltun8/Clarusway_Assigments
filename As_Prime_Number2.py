number = int(input("Enter a number please: "))
primes = []
for j in range(2,number):
    divisors = [i for i in range(2,j) if j % i == 0] #divisors collects the numbers which divides number evenly
    if divisors == []:
        primes.append(j)
print(primes)



