import itertools, sys

class Tree(object):
    def __init__(self):
        self.children = {}

    def add(self, xs):
        #self._add(xs + '$')
        self._add(xs)
        while len(xs) > 0:
            xs = xs[1:]
            #self._add(xs + '$')
            self._add(xs)

    def _add(self, xs):
        if len(xs) == 0:
            return
        if xs[0] not in self.children:
            self.children[xs[0]] = Tree()
        self.children[xs[0]]._add(xs[1:])

    def contains(self, xs):
        if xs == '':
            return True
        elif xs[0] in self.children:
            return self.children[xs[0]].contains(xs[1:])
        else:
            return False

    def __str__(self):
        return str(self.children)
    def __repr__(self):
        return str(self)

def prefix_tree(xs):
    ret = Tree()
    ret.add(xs)
    return ret

def substrings(xs):
    ret = set()
    for i in xrange(0, len(xs)):
        for j in xrange(i, len(xs)):
            ret.add(xs[i:j+1])
    return ret

if __name__ == '__main__':
    xs = sys.argv[1]
    needle = sys.argv[2]
    y = prefix_tree(xs)
    print xs, needle, y, y.contains(needle)
