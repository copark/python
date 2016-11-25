import sys

def fib(n): 
    a, b = 0, 1
    while b < n:
        b=a+b
        a=b
        print b
    print

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        fib(int(sys.argv[1]))
