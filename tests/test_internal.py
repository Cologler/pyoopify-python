# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import pytest

from pyoopify.internal import internal

import tests.pkg_for_internal as pfi

def test_internal_class_here():
    @internal
    class A:
        pass

    a = A()
    assert isinstance(A, type)
    assert isinstance(a, A)

def test_internal_class_somewhere():
    with pytest.raises(ImportError, match="is a internal class"):
        pfi.IClass()

def test_internal_func_here():
    @internal
    def func(*args, **kwargs):
        assert args == (1, 2)
        assert kwargs == {'a': 1}
        return 15

    assert func(1, 2, a=1) == 15

def test_internal_func_somewhere():
    with pytest.raises(ImportError, match="is a internal function"):
        pfi.func()
