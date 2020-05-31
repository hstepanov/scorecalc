#!/usr/bin/env python3
res_dict = {}
participant = ' '
while participant != '':
    participant = input('Input participant name:')
    res_dict.setdefault(participant, None)
print(res_dict)
