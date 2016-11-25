import operator

def test_func(arg):
    '''This is comments.'''
    return arg
def call_func(f, *args):
    return f(*args)

def test_call_func():
    print dir(operator)
    print call_func(operator.add, 4, 5)
    print call_func(operator.abs, -10)
    print call_func(lambda x, y: x + y, 4, 5)

def outer():
    def inner(a,b):
        return a+b
    return inner

def test_nested_func():
    f = outer()
    print f(10,20)

def better_outer():
    # count = 0
    count = [0]
    def inner():
        count[0] += 1
        return count[0]
    return inner

def test_lexical_scoping():
    c = better_outer()

    print c()
    print c()
    print c()

def Main():
    print "RUN %s" % __name__
    print test_func(1)
    print test_func(2)
    print test_func.__doc__
    test_call_func()
    test_nested_func()
    test_lexical_scoping()


if __name__ == '__main__':
    Main()
