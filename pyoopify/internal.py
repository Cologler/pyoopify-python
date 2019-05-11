# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import sys
import inspect
import functools
import types

NAME_INTERNAL_VARS = '__internal.vars__'

def _get_package_from_module(module):
    module_name = getattr(module, '__name__', None)
    if module_name is None:
        # dynamic module without name?
        return module
    package_name = module_name.partition('.')[0]
    if package_name == module_name:
        return module
    return sys.modules.get(package_name, module)

def _get_frame(frame_level: int):
    ' get frame from frame level '
    outerframes = inspect.getouterframes(inspect.currentframe())
    return outerframes[frame_level].frame

def _get_module(frame_level: int):
    ' get module from frame level '
    frame = _get_frame(frame_level+1)
    module = inspect.getmodule(frame)
    return module

def _get_package(frame_level: int):
    ' get top package from frame '
    return _get_package_from_module(_get_module(frame_level+1))


class InternalModuleType(types.ModuleType):
    def __getattribute__(self, name):
        if name == NAME_INTERNAL_VARS:
            raise AttributeError(name)
        internal_vars: dict = types.ModuleType.__getattribute__(self, NAME_INTERNAL_VARS)

        if name in internal_vars:
            # require package check
            if _get_package_from_module(self) is not _get_package(2):
                raise AttributeError(internal_vars[name])

        return types.ModuleType.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == NAME_INTERNAL_VARS:
            raise AttributeError(name)

        return super().__setattr__(name, value)


def internal(target):
    '''
    a internal decorator that use for prevent get target from package outside.

    for example, if a object defined in `a.b` marked internal,
    than only `a` and `a.*` can access it.
    if `b` try to access the object, raise `AttributeError`.
    '''

    key = target.__name__

    frame = _get_frame(2)
    is_on_module = frame.f_globals is frame.f_locals

    if is_on_module:
        module = inspect.getmodule(frame)
        module_type = type(module)
        internal_vars: dict = None

        if module_type is types.ModuleType:
            internal_vars = {}
            setattr(module, NAME_INTERNAL_VARS, internal_vars)
            module.__class__ = InternalModuleType

        elif module_type is InternalModuleType:
            internal_vars = types.ModuleType.__getattribute__(module, NAME_INTERNAL_VARS)

        else:
            raise RuntimeError

        if isinstance(target, type):
            target_type_desc = 'class'
        elif isinstance(target, types.FunctionType):
            target_type_desc = 'function'
        else:
            target_type_desc = 'object'

        internal_vars[key] = f'{key} is a internal {target_type_desc}'

    else:
        raise SyntaxError('@internal only allow to run on module level')

    return target
