def add_items(new_items, base_items=[]):
    for item in new_items:
        base_items.append(item)
    return base_items

def test_add_items():
    b=add_items((1,2,3))
    print b
    b2=add_items((1,2,3))
    print b2
    b3=add_items((1,2,3))
    print b3

def variable_function(*args, **kwargs):
    print 'args:', args
    print 'kwargs:', kwargs

def mixed_function(a, b, c=None, *args, **kwargs):
    print 'a,b,c:', (a,b,c)
    print 'args:', args
    print 'kwargs:', kwargs

def test_variable_function():
    variable_function('simple')
    variable_function(type='Complex')
    mixed_function(1,2,3,4,5,6,d=10,e=20,f=30)

def printer(a, b, c=0, d=None):
    print 'a: {0}, b: {1}, c: {2}, d: {3}'.format(a, b, c, d)

def test_unpack_argument():
    printer(2,3,4,5)
    ordered_args = (6,7)
    keyword_args = {'c':8, 'd':9}
    keyword_args2 = {'d':9}
    printer(*ordered_args, **keyword_args)

def Main():
    print "RUN %s" % __name__
    test_unpack_argument()


if __name__ == '__main__':
    Main()
