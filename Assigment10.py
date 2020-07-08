age = input("Are you a cigarette addict older than 75 years old?\n")
chronic = input("Do you have a severe chronic disease?\n")
immune = input("Is your immune system too weak?\n")

if (age == 'YES' and chronic == 'YES' and immune == 'YES'):
    print("You are in risky group")
else:
    print("You are not in risky group")
