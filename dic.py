#!/usr/bin/env python

'''
dictionaries is key/value hashtable
'''
def test_dic():
    print test_dic.__name__
    characters = {'hero': 'Othello', 'villain': 'Iago', 'friend': 'Cassio'}
    print characters

    key = 'villain'
    if key in characters:
        print '%s exists. value is %s' % (key, characters[key])

    characters['beauty'] = 'Desdemona'
    print characters

    characters['beauty'] = 'Update'
    print characters

    print "items test"
    print characters.items()

    print "iteritems test"

    s = set()
    for role, name in characters.iteritems():
        print role, name
        t = role,name
        s.add(t)

    print s
    l = list(s)
    print l

import itertools

def test_iter_tool():
    l1 = ['a', 'b', 'c']
    l2 = ['d', 'e', 'f']
    chain = itertools.chain(l1, l2)
    print [l for l in chain]
    for l in chain:
        print l


def Main():
    print "RUN %s" % __name__
    #test_dic()
    test_iter_tool()

if __name__ == '__main__':
    Main()
