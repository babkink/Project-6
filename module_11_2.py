import sys
import inspect
from inspect import isfunction, ismethod, isclass
from pprint import pprint

class TestClass:
    def printing(self):
        print('test')
    pass


def introspection_info(object):
    a = type(object)
    b = dir(object)
    c = inspect.getmodule(object)
    if isinstance(object, str):
        return object.upper(), a, b, c
    elif isinstance(object, list):
        object.append(10)
        return object, a, b, c
    elif isinstance(object, tuple):
        d = object.count('r')
        return object, a, b, c, d
    elif isfunction(object):
        return a, b, c, object.__name__
    elif ismethod(object):
        return a, b, c, object.__name__.capitalize()
    elif isclass(object):
        return a, b, c, object.__name__.upper()
    else:
        return a, b, c

tc = TestClass()

str_ = 'abcd'
list_ = [1,2,3,4,5]
tuple_ = ('q', 'w', 'e', 'r')

pprint(introspection_info(tc.printing))