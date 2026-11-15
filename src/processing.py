def filter_by_state(items: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей
    и фильтрует по заданному значению state 'EXECUTED' или 'CANCELED'"""

    new_list = []
    for i in items:
        if i.get("state") == state:
            new_list.append(i)
    return new_list


def sort_by_date(data_list: list, reverse: bool = True) -> list:
    """Функция сортирующая список по дате"""
    return [sorted(data_list, key=lambda x: x["date"], reverse=reverse)]
