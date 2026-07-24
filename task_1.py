import datetime

def get_days_from_today(date):
    today = datetime.date.today()
    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    delta = today - date_obj
    return delta.days

date = '2026-07-17'

print(get_days_from_today(date))