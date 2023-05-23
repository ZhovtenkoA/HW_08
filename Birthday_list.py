from datetime import datetime
from collections import defaultdict

users = {
    'Alex' : datetime(year = 1994, month = 11, day=1),
    'Anna' : datetime(year = 1995, month = 9, day = 29),
    'Alla' : datetime(year=1995, month=5, day=18),
    'Inna': datetime(year=1995, month=5, day=24),
    'Max': datetime(year=1995, month=5, day=25),
    'Yura': datetime(year=1995, month=5, day=26),
    'Lola': datetime(year=1995, month=5, day=27),
    'Olha': datetime(year=1995, month=5, day=28),
    'Ira' : datetime(year=1995, month=5, day=29),
    'Taras' : datetime(year=1995, month=5, day=30),
    'Nick': datetime(year=1995, month=5, day=31),
    
}


def get_birthdays_per_week(users):
    current_day = datetime.now()
    b_dict = defaultdict(list)
    for user, birthday in users.items():
        if current_day.month == birthday.month and current_day.day <= birthday.day and birthday.day in range(current_day.day + 8):
                if birthday.weekday() == 5:
                    birthday = datetime(year= birthday.year, month=birthday.month, day = birthday.day + 2)
                    b_dict[birthday.strftime('%A')].append(user)
                                     
                elif birthday.weekday() == 6:
                    birthday = datetime(
                        year=birthday.year, month=birthday.month, day=birthday.day + 1)
                    b_dict[birthday.strftime('%A')].append(user)
                                       
                elif birthday.weekday() < 5:
                    b_dict[birthday.strftime('%A')].append(user)
                    
    b_dict = dict(b_dict)
    unform_result = ''.join(f'{key}: {value}\n'for key, value in b_dict.items())
    result = unform_result.translate({ord(i):'' for i in "'[]"})

    return result

    
                    
print(get_birthdays_per_week(users))

