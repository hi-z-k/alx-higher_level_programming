#!/usr/bin/python3
''' module: 4-inherits_from '''


def inherits_from(obj, a_class):
    ''' the object is an instance of a class
    obj: an object
    a_class: a class
    returns: True if the object is an instance
		of a subclass, False otherwise.
    '''
    return (type(obj) != a_class and isinstance(obj, a_class))
