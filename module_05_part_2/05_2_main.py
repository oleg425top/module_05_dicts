import json
from module_05_part_2 import *
name = input('Введите ваше имя')
user_lvl = input("Выберите уровень сложности \nлегкий, средний, сложный: \n").lower()
test_words = get_user_level(user_lvl)
test_answers = base_program(test_words)
result = get_result(test_answers)
print(f"\nВаш ранг:\n{result}")



json_data = json.dumps(test_answers, ensure_ascii=False, indent=4)
with open(f'{name}.json', 'w', encoding='utf-8') as file:
    file.write(json_data)
# print(get_result(base_program(get_user_level(user_lvl))))
