#!/usr/bin/env python3
import sqlite3
#res_dict = {}
#participant = ' '
#while participant != '':
#    participant = input('Input participant name:')
#    res_dict.setdefault(participant, None)
#print(res_dict)

tours = int(input("Input tours number:"))
conn = sqlite3.connect("scorecalc.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS score_table
              (participant TEXT NOT NULL PRIMARY KEY)
               """)
for number in tours:
    num = int(1)
    query = 'ALTER TABLE {}
