data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей по значению ключа 'state'."""
    return [item for item in data if item.get("state") == state]


# Выход функции со статусом по умолчанию 'EXECUTED'
# print(filter_by_state(data))
# Вывод: [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Выход функции, если вторым аргументов передано 'CANCELED'
# print(filter_by_state(data, 'CANCELED'))
# Вывод: [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)


# Сортировка по убыванию (новые операции в начале)
sorted_desc = sort_by_date(data)
print(sorted_desc)

# Сортировка по возрастанию (старые операции в начале)
sorted_asc = sort_by_date(data, reverse=False)
print(sorted_asc)
