# -*- coding: utf-8 -*-
# lxf_decorator.py

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('---- Begin Call ----')
        result = func(*args, **kw)
        print('---- End Call ----')
        return result
    return wrapper

def log1(text=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('---- Begin Call ----')
            if text != '':
                print('%s %s()' % (text, func.__name__))
            result = func(*args, **kw)
            print('---- End Call ----')
            return result 
        return wrapper
    return decorator

@log1()
def test(message):
    print('This is a test function for decorator. The message passed into this function is below.')
    print(message)

def main():
    test('Hello guys! This decorator is amazing!')
    print('This function name is "%s".' % test.__name__)

if __name__ == '__main__':
    main()
