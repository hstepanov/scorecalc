#!/usr/bin/env python3
#
# Базовый функционал:
# - Пользовательский ввод данных по участникам (нужно сделать так-же \
#       добавление комманд и объединение участников по коммандам. \
#       Так-же необходимо выводить статистику по каждому туру для комманд, \
#       и итоговую статистику, с распределением мест по коммандам и участникам)
# - Добавление их в БД
# - Редактирование данных в БД, добавление данных по турам
# - Подсчёт результатов по каждому туру
# - Вывод результатов по каждому спортсмену
# - Вывод итоговых данных по всем турам, с распределением участников по местам

import sqlite3

# action section
act = input('Input you\'re choise:
             1 - Begin new competition
             2 - Begin new tour in current competition
             3 - Edit current data
            ')

# participant input section 
init_dict = {}
lst = []
while True:
    part_id = input("Порядковый номер участника: ")
    part_name = input("Имя участника: ")
    tpl = tuple([part_id, part_name])
    if part_id != '' and part_name.isalpha():
        lst.append(tpl)
    else:
        break
init_dict = dict(lst)

def create_db():
    conn = sqlite3.connect("scorecalc.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS scorecalc (part_id integer PRIMARY KEY, participant text, first_t integer, second_t integer)")
    conn.commit()
    conn.close()

def add_participant(part_id, part_name):
    conn = sqlite3.connect("scorecalc.db")
    cursor = conn.cursor()
    first_t, second_t = 0, 0
    cursor.execute("INSERT INTO scorecalc (part_id, participant, first_t, second_t) VALUES (?, ?, ?, ?)", (part_id, part_name, first_t, second_t))
    conn.commit()
    conn.close()

def tour_update():
    conn = sqlite3.connect("scorecalc.db")
    cursor = conn.cursor()
    tour_num = input("Номер тура: ")
    part_name = input("Имя участника: ")
    conn.commit()
    conn.close()
    
if act == '1':
    create_db()
    for key, value in init_dict.items():
        part_id = key
        part_name = init_dict[key]
        add_participant(part_id, part_name)
elif act == '2':
    pass
elif act == '3':
    pass

#conn = sqlite3.connect("scorecalc.db")
#cursor = conn.cursor()
#cursor.execute("SELECT * FROM scorecalc")
#print(cursor.fetchall())
#conn.close()
