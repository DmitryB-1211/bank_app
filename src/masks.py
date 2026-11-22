def get_mask_card_number(name_card: str) -> str:
    """Функция, которая принимает номер карты
    и выводит номер в формате XXXX XX** **** XXXX"""

    #проверка входных данных
    if not isinstance(name_card, str):
        raise TypeError("name_card должен быть строкой")
    if len(name_card) != 16 or name_card == "":
        raise ValueError("количество цифр должно быть 16")

    return name_card[0:4] + " " + name_card[4:6] + "** ****" + " " + name_card[12:]


def get_mask_account(name_card: str) -> str:
    """Функция, которая принимает номер карты
    и выводит номер в формате **XXXX"""

    #проверка входных данных
    if not isinstance(name_card, str):
        raise TypeError("name должен быть строкой")
    if len(name_card) != 16 or name_card == "":
        raise ValueError("количество цифр должно быть 16")

    return "**" + name_card[-4:]
