# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import pytest

from pyoopify.internal import internal

import tests.pkg_for_internal as pfi


@internal
class local_A:
    pass

def test_internal_class_here():
    a = local_A()
    assert isinstance(local_A, type)
    assert isinstance(a, local_A)

def test_internal_class_somewhere():
    with pytest.raises(AttributeError, match="InternalClass is a internal class"):
        pfi.InternalClass()

@internal
def local_func(*args, **kwargs):
    assert args == (1, 2)
    assert kwargs == {'a': 1}
    return 15

def test_internal_func_here():
    assert local_func(1, 2, a=1) == 15

def test_internal_func_somewhere():
    with pytest.raises(AttributeError, match="func is a internal function"):
        pfi.func()

class B:
    @internal
    def internal_method(self):
        return 12

def test_internal_method_here():
    b = B()
    assert b.internal_method() == 12

def test_internal_method_somewhere():
    pc = pfi.PublicClass()

    assert pc.public_method() == 'pm'
    with pytest.raises(AttributeError, match="internal_method is a internal function"):
        pc.internal_method()
