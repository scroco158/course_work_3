import util

# Загрузка данных
operations = util.operations_loading()

# Получаем список id номеров последних 5 операций
operations_for_print = util.operations_sort(operations)

# Печать операций
print()
util.print_operation(operations_for_print)
print()
