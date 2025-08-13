import random

def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list:
    """
    Генерує набір унікальних випадкових чисел у заданому діапазоні.

    :param min_value: мінімальне можливе число (не менше 1)
    :param max_value: максимальне можливе число (не більше 1000)
    :param quantity: кількість чисел для вибору (між min_value і max_value)
    :return: відсортований список унікальних чисел або порожній список, якщо параметри некоректні
    """
    # Перевірка вхідних параметрів
    if not (1 <= min_value <= max_value <= 1000):
        return []
    if not (min_value <= quantity <= max_value - min_value + 1):
        return []

    # Генерація унікальних чисел та сортування
    numbers = random.sample(range(min_value, max_value + 1), quantity)
    return sorted(numbers)


# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
