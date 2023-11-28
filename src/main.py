import utils
import os


print(os.getcwd())
# Загрузка данных
operations = utils.operations_loading()

# Получаем список id номеров последних 5 операций
operations_for_print = utils.operations_sort(operations)

# Печать операций
print()
utils.print_operation(operations_for_print)
print()
