import collections
import pprint

def test_import():
    d = collections.deque()
    d.append('a')
    d.appendleft('b')
    pprint.pprint(globals())

from collections import Set

def test_import_submodule():
    pass



def Main():
    print "RUN %s" % __name__
    test_import_submodule()




if __name__ == '__main__':
    Main()
