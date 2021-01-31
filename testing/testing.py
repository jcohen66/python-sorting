"""
python3 -m doctest testing.py -v
"""

class A:
    def f(self):
        '''
        Function description, argument types
        :return:
        >>> a = A()
        >>> a.f()
        Hello world
        'Hello world'
        '''
        print('Hello world')
        return 'Hello world'

    @property
    def error(self):
        '''
        This function just errors
        >>> A().error
        Traceback (most recent call last):
        ...
        Exception: I am an error
        '''
        raise Exception("I am an error")