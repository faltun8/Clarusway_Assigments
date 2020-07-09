while True:
    value = input("Bir sayi giriniz (Type 'q' and press enter for exit) : ")
    if (value != "q" ):
        if(value.isdigit()):
            value=int(value)
            power = len(str(value))
            basamak = len(str(value))
            sum = 0
            while basamak > 0:
                sum += (((value % (10 ** basamak)) // (10 ** (basamak - 1))) ** power)
                basamak -= 1
            if (sum == value):
                print(f"{value} is an Armstrong number.")
            else:
                print(f"{value} is not an Armstrong number.")
        else:
            print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    else:
        print("Bye..")
        break