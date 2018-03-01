# -*- coding: utf-8 -*-
import time, functools
def metric(func):
    @functools.wraps(func)
    def wrap(*args, **kw):
        start = time.time()
        func(*args, **kw)
        end = time.time()
        print('%s() 运行用了 %f' % (func.__name__, end-start))
        return func(*args, **kw)
    return wrap
