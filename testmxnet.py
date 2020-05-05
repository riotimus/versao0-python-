# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:21:38 2020

@author: JOHNJAIRO
"""

import mxnet as mx
a = mx.nd.ones((2, 3))
b = a * 2 + 1
b.asnumpy()
array([[ 3.,  3.,  3.],
       [ 3.,  3.,  3.]], dtype=float32)