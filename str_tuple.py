#!/usr/bin/env python
def test_split():
    print test_split.__name__
    s = 'abc.def'
    parts = s.split('.')
    print parts

def test_join():
    print test_join.__name__
    s = 'abc.def'
    parts = s.split('.')
    ns = '.'.join(parts)
    print ns

def test_tuples():
    print test_tuples.__name__
    t = ('hello', 'world')
    print t

    t = 'hello', 'world'
    print t

    h, w = t
    print h, w
    
    for c in t:
        print c

def Main():
    test_split()
    test_join()
    test_tuples()

if __name__ == '__main__':
    Main()
