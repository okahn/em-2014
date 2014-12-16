#!/usr/bin/python2

import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fin = open(sys.argv[1])
    else:
        fin = sys.stdin
    xs = map(str.strip, fin)
    xs.sort(lambda a, b: -1 if len(a) < len(b) else 1 if len(b) < len(a) else cmp(a, b))
    print '\n'.join(xs)
