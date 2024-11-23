from datetime import datetime


def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = input_date - today
        return delta.days
    except ValueError:
        raise ValueError("Wrong date format, please use 'YYYY-MM-DD'")


print(get_days_from_today("2025-10-09"))
