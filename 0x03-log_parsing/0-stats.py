#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics"""
import sys


code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
num_line = 1
size = [0]

for line in sys.stdin:
    line = line.rstrip()
    posc = line.split(' ')
    get_code = int(posc[7])
    size[0] += int(posc[8])
    if get_code in code:
        code[get_code] += 1
    if num_line % 10 == 0:
        print('File size: {}'.format(size[0]))
        for key in sorted(code.keys()):
            if code[key]:
                print('{}: {}'.format(key, code[key]))
    num_line += 1
