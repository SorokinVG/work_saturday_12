# Исходные данные
data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(data_list, state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data_list: Список словарей для фильтрации
    :param state: Значение статуса для фильтрации (по умолчанию 'EXECUTED')
    :return: Новый список словарей, соответствующих условию
    """
    return [item for item in data_list if item.get('state') == state]

def sort_by_date(data_list, reverse = True):
    """
    Сортирует список словарей по значению ключа 'date'.

    :param data_list: Список словарей для сортировки
    :param reverse: Порядок сортировки.
            True (по умолчанию) - по убыванию (сначала новые)
    :return: Новый отсортированный список словарей
    """
    return sorted(data_list, key=lambda item: item.get('date',''), reverse=reverse)


# 1. Вызов со статусом по умолчанию  'EXECUTED'
executed_items = filter_by_state(data)
print("По умолчанию (EXECUTED):")
print(executed_items)

# 2. Вызов с явным указанием статуса  'CANCELED'
canceled_items = filter_by_state(data, 'CANCELED')
print("\n С параметром (CANCELED):")
print(canceled_items)

# 3. Сортировка по дате по умолчанию (сперва самы последние)
sorted_desc = sort_by_date(data)
print("\n Сортировка по дате по убыванию (по умолчанию):")
print(sorted_desc)