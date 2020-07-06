# Part 1 - set nema and password
your_name = input('Please enter your name: ')
password = input('Please enter your password: ')
print('thank you your password has been set')

# Part 2 - Take name from user for checking
username = input('Please enter your name to learn your password: ')

# Part 3 - Check the username with db
if (your_name == username):
    print(f"Hello, {username}! The password is : {password}",)
else:
    print(f"Hello, {username}! See you later.")


