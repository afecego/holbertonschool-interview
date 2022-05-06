#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics"""
import sys


def stats():
    """print these statistics from the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size>
    Number of lines by status code:
    * possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
    * if a status code doesn’t appear or is not an integer, don’t print
    anything for this status code
    * format: <status code>: <number>
    * status codes should be printed in ascending order"""
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


if __name__ == '__main__':
    """Call the main function"""
    stats()
