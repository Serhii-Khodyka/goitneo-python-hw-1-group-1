from collections import defaultdict
from datetime import datetime, timedelta

user = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
        {"name": "Max Brand", "birthday": datetime(1980, 2, 25)},
        {"name": "Max Brand222", "birthday": datetime(1980, 2, 25)},
        {"name": "Jon Python", "birthday": datetime(1991, 3, 1)},
        {"name": "Tim Hilton", "birthday": datetime(1981, 3, 2)},
        {"name": "Nick Tailor", "birthday": datetime(1988, 2, 28)},
        {"name": "Sem Armstrong", "birthday": datetime(1964, 2, 24)}
]

def get_birthdays_list(users):
    birthday_dict = defaultdict()

    data_today = datetime.now()
    for num_user in users:
        name = num_user["name"]
        birthday = num_user["birthday"].date()  
        birthday_this_year = birthday.replace(year = data_today.year)

        day_of_week_today = data_today.weekday()
        
        data_today_friday = data_today + timedelta(days = 4 - day_of_week_today)
        
        #якщо буде кінець року, то +1 рік допоможе отримати правильний результат
        if birthday_this_year < data_today_friday.date():
            birthday_this_year = birthday.replace(year = data_today.year + 1)
    
        delta_days = (birthday_this_year - data_today_friday.date()).days

        #потрібно відфільтрувати з різницею в днях тиждень+субота+неділля поточного тижня
        if delta_days < 8:
            #якщо субота поточного тижня чи неділля чи понеділок - обєднуємо в понеділок
            week_day = "Monday" if delta_days < 4 else birthday_this_year.strftime("%A")
            if birthday_dict.get(week_day):
                birthday_dict[week_day].append(name)
            else:
                birthday_dict[week_day] = [name]
    #використовуємо сортування, щоб отримали по дням тижня
    for day in sorted(birthday_dict.keys(), key=lambda x: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].index(x)):
        print(f"{day}: {", ".join(birthday_dict[day])}")
        

if __name__ == "__main__":
    list_birthdays = get_birthdays_list(user)

