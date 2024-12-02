import json
from module_05_part_2 import *
name = input('Введите ваше имя')
user_lvl = input("Выберите уровень сложности \nлегкий, средний, сложный: \n").lower()
test_words = get_user_level(user_lvl)
test_answers = base_program(test_words)
result = get_result(test_answers)
print(f"\nВаш ранг:\n{result}")
create_json_files(test_answers, name)
print('Создан файл с вашими ответами')

