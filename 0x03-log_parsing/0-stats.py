#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

Input format:

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

(if the format is not this one, the line must be skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
    - Total file size: File size: <total size>
    - where <total size> is the sum of all previous <file size>
      (see input format above)

Number of lines by status code:
    - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
    - if a status code doesn’t appear or is not an integer,
      don’t print anything for this status code
    - format: <status code>: <number>
status codes should be printed in ascending order
"""
import sys


if __name__ == '__main__':
    badge = 0
    total_size = 0
    code_dict = {200: 0, 301: 0, 400: 0, 401: 0,
                 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            words = line.rstrip().split()
            if (len(words) != 9) or ('"GET' not in words) \
                    or ('HTTP/1.1"' not in words):
                continue
            code = int(words[-2])

            if code in code_dict:
                code_dict[code] += 1
            else:
                continue

            total_size += int(words[-1])
            badge += 1

            # Print stats after 10 badges
            if not badge % 10:
                print("File size: {}".format(total_size))
                total_size = 0
                keys = list(code_dict.keys())
                keys.sort()
                for key in keys:
                    if code_dict[key] > 0:
                        print("{}: {}".format(key, code_dict[key]))

    except KeyboardInterrupt:
        # Print stats after keyboard interrupt, works.
        print("File size: {}".format(total_size))
        total_size = 0
        for key in keys:
            if code_dict[key] > 0:
                print("{}: {}".format(key, code_dict[key]))
