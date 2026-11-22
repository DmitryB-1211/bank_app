from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(my_card: str) -> str:
    """Функция, обрабатывающая информацию о картах и о счетах"""
    card_in_parts = my_card.split(" ")
    number = card_in_parts[-1]
    name = " ".join(card_in_parts[:-1])

    # защита от некорректного ввода:
    if len(card_in_parts) < 2:
        raise ValueError("нет пробела")
    if not number.isdigit():
        raise TypeError("number должен быть числовой")

    # релизация функции
    if "счет" in name.lower() or "счёт" in name.lower():
        return f"{name} {get_mask_account(number)}"

    return f"{name} {get_mask_card_number(number)}"


def get_date(data: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате
    '2024-03-11T02:26:18.671407' и возвращает строку
    с датой в формате 'ДД.ММ.ГГГГ'"""

    if data == '':
        raise ValueError("некорректный ввод")

    if not isinstance(data, str):
        raise TypeError("name должен быть строкой")

    return data[8:10] + "." + data[5:7] + "." + data[0:4]

