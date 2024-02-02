import sys
def get_func_class(func):
    classes = []
    parent = sys.modules[func.__module__]
    names = func.__qualname__.split('.')[:-1]
    for n in names:
        parent = parent.__dict__[n]
        if isinstance(parent, type):
            classes.append(parent)
    return classes[-1] if classes else None
def inspect_type(func):
    ftype = None
    if func.__name__ == func.__qualname__:
        return 'function', None #no self
    elif '.<locals>' in func.__qualname__:
        return 'function', None #no self
    cls = get_func_class(func)
    ftype = cls.__dict__.get(func.__name__)
    if type(ftype) == staticmethod:
        return 'staticmethod', cls #no self
    elif type(ftype) == classmethod:
        return 'classmethod', cls #self
    elif ftype.__class__.__name__ == 'function':
        return 'instancemethod', cls #cls(self)
    else:
        raise TypeError('Unknown Type %s, Please check input is method or function' % func)