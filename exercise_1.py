# Tunik Olexandr group 4
from datetime import datetime

def get_days_from_today(date):
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        
        today = datetime.today().date()
        
        delta = today - target_date
        
        return delta.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."

# Приклади використання
print(get_days_from_today("2021-10-09"))  # Має повернути кількість днів до цієї дати
print(get_days_from_today("2020-10-09"))  # Має повернути кількість днів з цієї дати
print(get_days_from_today("2021-13-09"))  # Неправильний формат дати
