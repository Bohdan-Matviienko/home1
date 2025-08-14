import random

def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list[int]:
    """
    Генерує відсортований список унікальних випадкових чисел у заданому діапазоні.
    Повертає [] якщо параметри некоректні.

    :param min_value: мінімальне можливе число (не менше 1)
    :param max_value: максимальне можливе число (не більше 1000)
    :param quantity: кількість чисел для вибору (1 <= quantity <= кількість чисел у діапазоні)
    :return: відсортований список унікальних чисел або []
    """
    # Перевірка типів
    if not all(isinstance(x, int) for x in (min_value, max_value, quantity)):
        return []

    # Перевірка діапазону
    if not (1 <= min_value <= max_value <= 1000):
        return []

    # Перевірка кількості чисел
    possible_numbers = max_value - min_value + 1
    if not (1 <= quantity <= possible_numbers):
        return []

    # Генерація випадкових унікальних чисел
    numbers = random.sample(range(min_value, max_value + 1), quantity)
    return sorted(numbers)


# Приклади використання
print(get_numbers_ticket(10, 20, 5))   # Коректно
print(get_numbers_ticket(1, 49, 6))    # Коректно
print(get_numbers_ticket(1, 10, 15))   # Некоректно → []
