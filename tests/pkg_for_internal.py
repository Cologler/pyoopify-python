# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from pyoopify.internal import internal

@internal
class InternalClass:
    def func(self):
        pass

@internal
def func(*args, **kwargs):
    pass

class PublicClass:
    def public_method(self):
        return 'pm'

    @internal
    def internal_method(self):
        return 'im'
