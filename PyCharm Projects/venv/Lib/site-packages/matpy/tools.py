#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

@version: 0.1
@author:  quantpy
@file:    tools.py
@time:    2018/4/10 13:22
"""

from copy import deepcopy as copy
from collections import abc
import numpy as np

import matlab.engine
from matlab import mlarray


def name_of(v): return v.__class__.__name__


def py2mat(v):
    """
    change a python variable to matlab variable
    list -> cell
    ndarray -> matrix
    dict -> struct
    """
    v = copy(v)
    c_name = name_of(v)
    if c_name in ('DataFrame', 'Series'):
        v = v.values
        c_name = name_of(v)

    if c_name == 'ndarray':
        return matlab.double(v.tolist())

    if isinstance(v, abc.Mapping):
        for k, v_ in v.items():
            v[k] = py2mat(v_)

    if isinstance(v, abc.MutableSequence):
        v = list(v)
        for i, v_ in enumerate(v):
            v[i] = py2mat(v_)

    return v


def mat2py(v):
    """change a matlab variable to python variable"""
    if isinstance(v, abc.MutableSequence):
        for i, v_ in enumerate(v):
            v[i] = mat2py(v_)
    elif isinstance(v, abc.Mapping):
        for k, v_ in v.items():
            v[k] = mat2py(v_)

    elif name_of(v) in tuple(t for t in dir(mlarray) if not t.startswith('_')):
        v = np.array(v)

    return v

