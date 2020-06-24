import sqlite3
#part_dict = {}
#participant = None
#''' whitespase is the end of input'''
#while participant != '':
#  participant = input('input name:')
#  if participant.isalpha():
#    part_dict.setdefault(participant, None)
#  else:
#    break
#
#print(part_dict)
tours_num = int(input("Input number of tours:"))
conn = sqlite3.connect("scorecalc.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS scorecalc
                  (id integer NOT NULL PRIMARY KEY, 
                   participant text, 
                   first_t integer, second_t integer)
               """)
conn.commit()

def add_participant(part_name):
  first_t, second_t = 0
  id = 1
  while part_name.isalpha():
    cursor.execute("""INSERT INTO scorecalc
                      VALUES (?, ?, ?, ?);
                   """)
    conn.commit()
    id += 1
    
conn.close()
