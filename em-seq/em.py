def suffixes(w):
    for i in reversed(xrange(len(w))):
        yield w[i:]

def flip(x):
    if x == '0':
        return '1'
    return '0'

def core():
    yield (None, '0')
    yield ('', '1')
    yield ('', '0')
    seq = '010'
    while True:
        last = ''
        last_pos = -1
        for t in suffixes(seq):
            latest = seq[:-1].rfind(t)
            if latest != -1:
                last = t
                last_pos = latest
            else:
                break
        #print last, seq[last_pos:], seq[last_pos + len(last)]
        ret = flip(seq[last_pos + len(last)])
        seq += ret
        yield (last, ret)

longest = 0

if __name__ == '__main__':
    x = core()
    next(x)
    for i in xrange(100000):
        t = next(x)[0]
        longest = max(longest, len(t))
        if len(t) >= longest:
            print t.rjust(30)
