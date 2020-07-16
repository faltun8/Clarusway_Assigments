def parrot_trouble(talking, hour):
    if talking == True and not 21 > hour > 6:
        return True
    else:
        return False
