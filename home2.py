from datetime import datetime

def get_days_from_today(date_str: str) -> int:
    """
    Розраховує кількість днів між заданою датою і поточною датою.
    
    :param date_str: рядок дати у форматі 'YYYY-MM-DD'
    :return: кількість днів (int), від’ємне значення — якщо дата у майбутньому
    """
    try:
        # Перетворюємо рядок на об'єкт datetime
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Дата повинна бути у форматі 'YYYY-MM-DD'")
    
    # Поточна дата (без часу)
    today = datetime.today().date()
    
    # Різниця в днях
    delta = today - given_date
    return delta.days


# Приклади використання:
print(get_days_from_today("2020-10-09"))  # Наприклад, може вивести позитивне число
print(get_days_from_today("2030-01-01"))  # Виведе від’ємне число, якщо дата у майбутньому
