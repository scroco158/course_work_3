import util

# Загрузка данных
operations = util.operations_loading()

# Получаем список id номеров последних 5 операций
latest_operations_id = util.operations_sort(operations)

# Печать операций
print()
for item in latest_operations_id:
    util.print_operation(item, operations)
    print()
