import json

def get_user_level(user_level):
    with open('questions.json', 'r', encoding='utf-8') as file:
        data_level = json.load(file)
        questions = data_level[0]["questions"]
        words_easy = questions[0]
        words_medium = questions[1]
        words_hard = questions[2]
    if user_level == 'средний':
        level_dict = words_medium
    elif user_level == 'сложный':
        level_dict = words_hard
    else:
        level_dict = words_easy
    return level_dict

def base_program(get_user_level_dict:dict):
    answers = {}
    for word in get_user_level_dict:
        user_answer = input(f'перевод слова {word}, это слово из {len(get_user_level_dict.setdefault(word))} букв первая буква {get_user_level_dict.get(word)[0]} ')
        if user_answer == get_user_level_dict.setdefault(word):
            print(f'верно {word} это {get_user_level_dict.setdefault(word)}')
            answers.update({word:True})
        else:
            print(f'неверно {word} это {get_user_level_dict.setdefault(word)}')
            answers.update({word:False})
    return answers


def get_result(answers_dict:dict):
    with open('questions.json', 'r', encoding='utf-8') as file:
        data_level = json.load(file)
        level_data = data_level[1]["levels"]
    global f
    count_right_answers = 0

    for answer in answers_dict:
        if answers_dict.setdefault(answer):
            print(f' {answer} - отвечено верно')
            count_right_answers += 1
        else:
            print(f' {answer} - отвечено неверно')
    f = f'{level_data.setdefault(str(count_right_answers))}'
    return f'{level_data.setdefault(str(count_right_answers))}'

def create_json_files(test_answers:dict, name):
    test_answers.update({f'{name}': f'{f}'})
    json_data = json.dumps(test_answers, ensure_ascii=False, indent=4)
    with open(f'{name}.json', 'w', encoding='utf-8') as file:
        file.write(json_data)


