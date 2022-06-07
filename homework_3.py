# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c англи
# йского на русский язык. Например:
def num_translate(i):
    translate_book = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
        "eleven": "одиннадцать",
        "twelve": "двенадцать",
        "thirteen": "тринадцать",
        "fourteen": "четырнадцать",
        "fifteen": "пятнадцать",
    }
    if i.istitle():
        return translate_book[i.lower()].title()
    else:
        return translate_book[i]

score = input('Value:')
print(num_translate(score))

#3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудни
# ков и возвращающую словарь, в котором ключи — первые буквы имён, а значения — сп
# иски, содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребу
# ется сортировка по ключам? Можно ли использовать словарь в этом случае?

def thesaurus(*names):
    name_list = [*names]
    res = {}
    for name in name_list:
        name.capitalize()
        capital = name[0]
        if capital in res.keys():
            res[capital].append(name)
        else:
            res_1 = [name]
            res[capital] = res_1

    return res

print(thesaurus("Иван", "Мария", "Петр", "Илья"))

#5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех 
# случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]

import random as rd

def get_jokes(joke_count):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 0
    spc = ' '
    while i != joke_count:
        joke = nouns[rd.randint(0, 4)] + spc + adverbs[rd.randint(0, 4)] + spc + adjectives[rd.randint(0, 4)]
        print(joke)
        i += 1

get_jokes(6)



