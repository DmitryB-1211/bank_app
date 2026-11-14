def filter_by_state(items: list, state='EXECUTED'):
    '''Функция принимает список словарей
    и фильтрует по заданному значению state 'EXECUTED' или 'CANCELED' '''

    new_list = []
    for i in items:
        if i.get('state') == state:
            new_list.append(i)
    return new_list


def sort_by_date(data_list: list, reverse=True):
    ''' Функция сортирующая список по дате'''
    return [sorted(data_list, key=lambda x: x['date'], reverse=reverse)]


#data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

#print(sort_by_date(data, reverse=True))
