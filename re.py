import re
def Main():
    text = 'All your base are belong to us.'
    print re.search(r'o\s?u', text)
    print re.findall(r'o\s?u', text)
    pass

if __name__ == '__main__':
    Main()
