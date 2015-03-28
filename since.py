#!/usr/bin/env python3

import datetime
import re
import sys


def main(strTime):
    now = datetime.datetime.now()
    pattern = r'(\d\d):(\d\d)'
    match = re.match(pattern, strTime)
    time = datetime.datetime(
        now.year,
        now.month,
        now.day,
        int(match.group(1)),
        int(match.group(2)))
    diff = now - time
    if diff.total_seconds() < 0:
        return now - time + datetime.timedelta(1)
    return diff

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage {0} {{time}}'.format(sys.argv[0]))
    else:
        print(main(sys.argv[1]))
