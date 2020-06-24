#!/usr/bin/env python3
import sqlite3
from sys import argv
part_id = int(input("input participant id: "))
part_name = input("input participant name: ")

conn = sqlite3.connect("scorecalc.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS scorecalc (part_id integer NOT NULL PRIMARY KEY, participant text, first_t integer, second_t integer)")
conn.commit()

def add_participant(part_id, part_name):
    first_t, second_t = 0, 0
    cursor.execute("INSERT INTO scorecalc (part_id, participant, first_t, second_t) VALUES (?, ?, ?, ?)", (part_id, part_name, first_t, second_t))
    conn.commit()

add_participant(part_id, part_name)
cursor.execute("SELECT * FROM scorecalc")
print(cursor.fetchall())
conn.close()
