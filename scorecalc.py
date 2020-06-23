#!/usr/bin/env python3
#res_dict = {}
#participant = ' '
#while participant != '':
#    participant = input('Input participant name:')
#    res_dict.setdefault(participant, None)
#print(res_dict)

import sqlite3

conn = sqlite3.connect("scorecalc.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS
                  participants(id int PRIMARY KEY, name text NOT NULL)
               """)
conn.commit()

cursor.execute("SELECT * FROM participants")

conn.close()
