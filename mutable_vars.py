from copy import copy, deepcopy

# Пример 1: Функция, изменяющая неизменяемые значения в глобальной переменной
def modify_immutable(global_variable, num):
    global_variable['key1'] = 'new_value'
    global_variable['key2'] = 42
    num += 20

# Пример 2: Функция, изменяющая изменяемые значения в глобальной переменной
def modify_mutable(global_variable):
    global_variable['nested_dict']['nested_key'] = 'modified_value'
    global_variable['list'].append(100)

def modify_copies(copy_dict):
    copy_dict['key1'] += ' sauce'

# Пример использования:
if __name__ == "__main__":
    # Глобальная переменная, состоящая из изменяемых и неизменяемых значений
    my_global_variable = {'key1': 'value1', 'key2': 20, 'nested_dict': {'nested_key': 'nested_value'}, 'list': [1, 2, 3]}

    immutable_num = 12

    print("Изначальная глобальная переменная:", my_global_variable)
    print("Init num:", immutable_num)

    # Вызываем первую функцию, которая изменяет неизменяемые значения
    modify_immutable(my_global_variable, immutable_num)
    print("Глобальная переменная после вызова modify_immutable:", my_global_variable)
    print("Init num:", immutable_num)

    # Вызываем вторую функцию, которая изменяет изменяемые значения
    modify_mutable(my_global_variable)
    print("Глобальная переменная после вызова modify_mutable:", my_global_variable)

