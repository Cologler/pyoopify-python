# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import pytest

from pyoopify.final import final

def test_final_decorator():
    @final
    class A:
        pass

    with pytest.raises(TypeError):
        class B(A):
            pass

    with pytest.raises(TypeError):
        @final
        class C(A):
            pass
