import datetime

def age_calculater(birth_day):
    birth_day_list = birth_day.split("/")
    birth_day_obj = datetime.datetime(year=int(birth_day_list[2]),month=int(birth_day_list[1]),day=int(birth_day_list[0]))
    today = datetime.datetime.today()
    age = (int((today - birth_day_obj).days)/365) - (int((today - birth_day_obj).days) / 365) % 1
    return age

print(age_calculater("22/5/2000"))