# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from pyoopify.internal import internal

@internal
class IClass:
    def func(self):
        pass

@internal
def func(*args, **kwargs):
    pass
