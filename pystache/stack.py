# coding: utf-8
from copy import (copy)

class Nothing(object):
    """ A sentinal object for when things don't exist. """
    pass
_NOTHING = Nothing()

class Stack(list):
    def __init__(self, obj=_NOTHING, *args, **kwargs):
        super(list, self).__init__(*args, **kwargs)
        if not isinstance(obj, Nothing):
            self.append(obj)
    
    def __call__(self, _copy=False):
        if _copy:
            return copy(self[-1])
        else:
            return self[-1]

    def push(self, *args, **kwargs):
        return self.append(*args, **kwargs)

