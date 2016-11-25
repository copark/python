#!/usr/bin/env python
import os

def getSize(file):
    file.seek(0, 2)
    size = file.tell()
    return size

def getSize2(path):
    return os.stat(path).st_size

def test_file_io():
    colors = ['red\n', 'yellow\n', 'blue\n']
    f = open('colors.txt', 'w')

    print dir(f)
    f.writelines(colors)
    f.close()

    f = open('colors.txt')
    print(f.readline())
    print(f.readline())
    print(f.readline())
    f.close()

    f = open('colors.txt')
    print(f.readlines())
    f.close()

    f = open('colors.txt')
    print getSize(f)
    print getSize2('colors.txt')

def Main():
    print "RUN %s" % __name__
    test_file_io()

if __name__ == '__main__':
    Main()
