from masks import get_mask_card_number, get_mask_account

def mask_account_card(my_card: str):
    """Функция, обрабатывающая информацию о картах и о счетах"""
    card_in_parts = my_card.split(' ')
    number = card_in_parts[-1]
    name = ' '.join(card_in_parts[:-1])
    #print(len(card_in_parts))
    #print(card_in_parts)
    #print(number)

    #защита от некорректного ввода:
    if len(card_in_parts) < 2:
        return 'не корректный номер карты'
    if len(number) != 16 and len(number) != 20:
        return 'не корректный номер карты'

    #релизация функции
    if 'счет' in name.lower() or 'счёт' in name.lower():
        return f"{name} {get_mask_account(number)}"

    return f"{name} {get_mask_card_number(number)}"


#print(mask_account_card('счёт73654108430135874305'))
#print(mask_account_card('Platinum card 7000792289606361'))


def get_date(data: str):
    """Функция, которая принимает на вход строку с датой в формате 
        '2024-03-11T02:26:18.671407' и возвращает строку
        с датой в формате 'ДД.ММ.ГГГГ' """
    return data[8:10] + '.' + data[5:7] + '.' + data[0:4]


#print(get_date('2024-03-11T02:26:18.671407'))