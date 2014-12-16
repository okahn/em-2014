#!/usr/bin/python2

import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fin = open(sys.argv[1])
    else:
        fin = sys.stdin
    xs = map(str.strip, fin.readlines())

    if len(xs) == 0:
        sys.exit(0)

    ll = len(xs[0])
    n = 1
    for line in xs[1:]:
        if ll !=
