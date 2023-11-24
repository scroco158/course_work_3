import json


def operations_loading():
    """Загружает данные по операциям из файла"""
    with open('/home/user/PycharmProjects/course_work_3/data/operations.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def operations_sort(operations):
    """Выбирает последние 5 выполненных операций пользователя и возвращает список их id"""
    exec_operations = [item for item in operations if ('state' in item.keys()) and (item['state'] == "EXECUTED")]
    exec_operations_sorted = sorted(exec_operations, key=lambda operation: operation['date'], reverse=True)
    latest_operations = [exec_operations_sorted[i]['id'] for i in range(0, 5)]
    return latest_operations


operations = operations_loading()
latest_operation_id = operations_sort(operations)

print(latest_operation_id)
