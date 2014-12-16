import sys

needle = sys.argv[1]
xs = open('seq.out').read().replace('\n','').strip()
out = ''

for i in xrange(len(xs)):
    if xs[i:].startswith(needle):
        try:
            out += xs[i+len(needle)]
        except IndexError:
            pass
print out
