#!/usr/bin/env python

def test_list():
    print test_list.__name__
    l = list('abcde')
    for i in range(len(l)):
        print i, l[i]



def test_reverse_list():
    print test_reverse_list.__name__
    l = list('abcde')
    for i in range(1, len(l)+1):
        print i, l[-i]

def test_slice():
    print test_slice.__name__
    l = list('abcdefgh')
    print  l[1:-1:2]

def Main():
    test_list()
    test_reverse_list()
    test_slice();

if __name__ == '__main__':
    Main()
