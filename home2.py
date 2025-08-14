from datetime import datetime, date

def get_days_from_today(date_str: str, *, on_error=None) -> int | None:
    """
    Розраховує кількість днів між заданою датою і поточною датою.

    :param date_str: рядок дати у форматі 'YYYY-MM-DD'
    :param on_error: що повернути при некоректних даних (за замовчуванням None)
    :return: кількість днів (int), від'ємне — якщо дата у майбутньому; або on_error при помилці
    """
    try:
        given_date = datetime.strptime(str(date_str).strip(), "%Y-%m-%d").date()
    except (ValueError, TypeError, AttributeError):
        # НЕКОРЕКТНІ ДАНІ → не кидаємо помилку, а повертаємо on_error
        return on_error

    today = date.today()  # Лише дата, без часу
    return (today - given_date).days


# Приклади використання:
print(get_days_from_today("2021-10-09"))            # коректний ввід → int
print(get_days_from_today("2021-13-09"))            # некоректний місяць → None
print(get_days_from_today("2021/10/09", on_error=0))# інший формат → 0 (не падає програма)
