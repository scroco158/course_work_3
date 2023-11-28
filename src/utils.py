import json
import os

def operations_loading():
    """Загружает данные по операциям из файла"""
    with open(os.path.abspath('./data/operations.json'), 'r', encoding='utf-8') as file:
        return json.load(file)


def operations_sort(operations):
    """Выбирает последние 5 выполненных операций пользователя и возвращает их"""
    exec_operations = [item for item in operations if ('state' in item.keys()) and (item['state'] == "EXECUTED")]
    exec_operations_sorted = sorted(exec_operations, key=lambda operation: operation['date'], reverse=True)
    latest_operations = [exec_operations_sorted[i] for i in range(0, 5)]
    return latest_operations


def print_operation(operations_for_print):
    """ Распечатывает операцию по ее номеру в формате требуемом по ТЗ"""
    for item in operations_for_print:
        if 'date' in item:
            print(item['date'][8:10]+'.'+item['date'][5:7]+'.'+item['date'][0:4], end=' ')
        if 'description' in item:
            print(item['description'])
        if 'from' in item:
            print(item['from'][:-12], item['from'][-12:-10] + '**', '****', item['from'][-4:], '-> ', end='')
        if 'to' in item:
            print(item['to'][:-21], '**' + item['to'][-4:])
        if 'operationAmount' in item:
            print(item['operationAmount']['amount'], item['operationAmount']['currency']['name'])
        print()
