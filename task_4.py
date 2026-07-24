from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """Повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата')."""
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays

# Перевірка
users = [
    {"name": "John Doe", "birthday": "1985.07.23"},
    {"name": "Jane Smith", "birthday": "1990.07.28"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
