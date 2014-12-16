# NN = 10**6

def factor(w):
    i = 0
    j = i + 1
    while j <= len(w):
        if w[i:j] in w[:i]:
            j += 1
        else:
            if j > 2: j -= 1
            yield w[i:j]
            i = j
    yield w[i:]

if __name__ == '__main__':
    # print list(factor('abbaabbbaaabab'))
    # print list(factor(raw_input('>')))
    ws = open('../projects/em-seq/gen/foo.out').read()
    # ws = open('../projects/em-seq/seq.out').read()
    for x in factor(ws.replace('\n', '').strip()):
        print len(x), x
