words_easy = {
      "family": "семья",
      "hand": "рука",
      "people": "люди",
      "evening": "вечер",
      "minute": "минута",
}
words_medium = {
      "believe": "верить",
      "feel": "чувствовать",
      "make": "делать",
      "open": "открывать",
      "think": "думать",
}
words_hard = {
      "rural": "деревенский",
      "fortune": "удача",
      "exercise": "упражнение",
      "suggest": "предлагать",
      "except": "кроме",
}
levels = {
      0: "Нулевой",
      1: "Так себе",
      2: "Можно лучше",
      3: "Норм",
      4: "Хорошо",
      5: "Отлично"
}


def get_user_level(user_level):
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
    count_right_answers = 0
    for answer in answers_dict:
        if answers_dict.setdefault(answer):
            print(f' {answer} - отвечено верно')
            count_right_answers += 1
        else:
            print(f' {answer} - отвечено неверно')
    return f'ваш уровень знаний {levels.setdefault(count_right_answers)}'




