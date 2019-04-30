# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

def final(cls):
    '''
    a final decorator that use for prevent inherit.
    '''
    def __init_subclass__(cls, *args, **kwargs):
        raise TypeError('unable to inherit final class')

    cls.__init_subclass__ = __init_subclass__

sealed = final
