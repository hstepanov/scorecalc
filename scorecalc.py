#!/usr/bin/env python3
# Базовый функционал:
# - Пользовательский ввод данных
# - Добавление их в БД
# - Добавление данных по турам
# - Подсчёт результатов по каждому туру
# - Вывод результатов по каждому спортсмену

import sqlite3
from sys import argv
# need to make unbreakable input of valid data
init_dict = {}
lst = []
while True:
    part_id = input("input participant id: ")
    part_name = input("input participant name: ")
    tpl = tuple([part_id, part_name])
    if part_id != '' and part_name.isalpha():
        lst.append(tpl)
    else:
        break
init_dict = dict(lst)
print(init_dict)

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

create_db()
for key, value in init_dict.items():
    part_id = key
    part_name = init_dict[key]
    add_participant(part_id, part_name)


conn = sqlite3.connect("scorecalc.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM scorecalc")
print(cursor.fetchall())
conn.close()
