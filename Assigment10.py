age = input("Are you a cigarette addict older than 75 years old?\n").title().strip()
chronic = input("Do you have a severe chronic disease?\n").title().strip()
immune = input("Is your immune system too weak?\n").title().strip()

if (age == 'Yes' or chronic == 'Yes' or immune == 'Yes'):
    print("You are in the risky group")
else:
    print("You are not in the risky group")

