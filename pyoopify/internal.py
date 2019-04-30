# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import sys
import inspect
import functools


def _get_package_from_frame(frame):
    module = inspect.getmodule(frame)
    packagename = module.__name__.partition('.')[0]
    package = sys.modules[packagename]
    return package

def _get_package(frame_level):
    outerframes = inspect.getouterframes(inspect.currentframe())
    frame = outerframes[frame_level].frame
    package = _get_package_from_frame(frame)
    return package

def internal(target):
    '''
    a internal decorator that use for prevent get target from package outter.
    '''

    key = f'__pkgvar.{id(target)}'

    package = _get_package(2)
    setattr(package, key, True)

    if isinstance(target, type):
        def init(*args, **kwargs):
            package = _get_package(2)
            if not hasattr(package, key):
                raise ImportError(f'{target!r} is a internal class')
            target.__init__(*args, **kwargs)

        cls = type(target.__name__, (target, ), {
            '__init__': init
        })

        return functools.update_wrapper(cls, target, updated=())

    elif callable(target): # function
        def wrapper(*args, **kwargs):
            package = _get_package(2)
            if not hasattr(package, key):
                raise ImportError(f'{target!r} is a internal function')
            return target(*args, **kwargs)

        return functools.update_wrapper(wrapper, target)

    else: # object instance
        raise NotImplementedError
