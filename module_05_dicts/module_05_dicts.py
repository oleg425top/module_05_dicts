'''Домашнее задание часть первая '''
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
level = input('выберите уровень сложности: легкий, средний или тяжелый')
words =[]
if level.lower() == 'средний':
    words = words_medium
elif level.lower() == 'тяжелый':
    words = words_hard
else:
    words = words_easy

correct = []
incorrect = []
count = 0

for word in words:

    answer = input(f'перевод слова {word}, это слово из {len(words.setdefault(word))} букв первая буква {words.get(word)[0]} ')

    if answer == words.setdefault(word).lower():
        print(f'верно {word} это {words.get(word)} ')
        correct.append(word)
        words[word] = True
        count += 1
    else:
        print(f'неверно {word} это {words.get(word)} ')
        incorrect.append(word)
        words[word] = False

print('вы верно ответили на ')
print(*correct, sep=',')
print('вы неверно ответили на:')
print(*incorrect, sep=',')
print(f'ваш уровень {levels.get(count)}')
