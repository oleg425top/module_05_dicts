from module_05_part_2 import *

user_lvl = input("Выберите уровень сложности \nлегкий, средний, сложный: \n").lower()

print(get_result(base_program(get_user_level(user_lvl))))
