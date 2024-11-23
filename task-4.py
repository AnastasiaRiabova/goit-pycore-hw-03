from datetime import datetime, timedelta


def get_upcoming_birthdays(users):

    today = datetime.today().date()
    next_week = today + timedelta(days=7)
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= next_week:
            if birthday_this_year.weekday() in (5, 6):
                offset = 7 - birthday_this_year.weekday()
                congratulation_date = birthday_this_year + timedelta(days=offset)
            else:
                congratulation_date = birthday_this_year

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [{"name": "John Doe", "birthday": "1985.12.30"}, {"name": "Jane Doe", "birthday": "1985.12.29"}]
print(get_upcoming_birthdays(users))
