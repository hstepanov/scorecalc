#!/usr/bin/env python3
import sqlite3
from sys import argv
# need to make unbreakable input of valid data
while True:
    init_list = []
    appending_list = []
    part_id = int(input("input participant id: "))
    part_name = input("input participant name: ")
    if part_name.isalpha():
        appending_list.append(part_id)
        appending_list.append(part_name)
        init_list.append(appending_list)
        appending_list.clear()
    else:
        break
print(init_list)

conn = sqlite3.connect("scorecalc.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS scorecalc (part_id integer PRIMARY KEY, participant text, first_t integer, second_t integer)")
conn.commit()

def add_participant(part_id, part_name):
    first_t, second_t = 0, 0
    cursor.execute("INSERT INTO scorecalc (part_id, participant, first_t, second_t) VALUES (?, ?, ?, ?)", (part_id, part_name, first_t, second_t))
    conn.commit()

#while part_name.isalpha():
add_participant(part_id, part_name)

cursor.execute("SELECT * FROM scorecalc")
print(cursor.fetchall())
conn.close()
