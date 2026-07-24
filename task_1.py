import datetime

def get_days_from_today(date: str) -> int | None:
    """Розраховує кількість днів між поточною датою та заданою датою."""
    try:
        target_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.date.today()

        return (today - target_date).days
    except ValueError:
        print(f"Неправильний формат дати: {date}. Використовуйте формат 'YYYY-MM-DD'.")
        return None
        
    
    
    


print(get_days_from_today('2026-05-24'))
print(get_days_from_today('2026-10-12'))
print(get_days_from_today("2026-11-45"))