import itertools, sys

LOTS = 20

def flatten(xss):
    ret = []
    for xs in xss:
        ret += xs
    return ret

def count(haystack, needle):
    ret = 0
    for i in xrange(len(haystack)):
        if haystack[i:i + len(needle)] == needle:
            ret += 1
    return ret

em = open('../seq.out').read().replace('\n', '').strip()

#needle = sys.argv[1]

#a, b = em.find(needle + '0'), em.find(needle + '1')

#print em[:max(a, b) + len(needle)].count(needle), a, b
for w in flatten(list((map(''.join, itertools.product(('0', '1'), repeat=k)) for k in xrange(LOTS)))):

    needle = w
    a, b = em.find(needle + '0'), em.find(needle + '1')
    print needle, count(em[:max(a, b) + len(needle)], needle), a, b
    if needle == '': continue
    assert count(em[:max(a, b) + len(needle)], needle) == 2
