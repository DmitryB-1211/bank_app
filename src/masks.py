def get_mask_card_number(name_card: str) -> str:
    """Функция, которая принимает номер карты
    и выводит номер в формате XXXX XX** **** XXXX"""
    return name_card[0:4] + " " + name_card[4:6] + "** ****" + " " + name_card[12:]


def get_mask_account(name_card: str) -> str:
    """Функция, которая принимает номер карты
    и выводит номер в формате **XXXX"""
    return "**" + name_card[-4:]
