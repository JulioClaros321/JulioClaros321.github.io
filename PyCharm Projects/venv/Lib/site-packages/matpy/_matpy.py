#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

@version: 0.1
@author:  quantpy
@file:    _matpy.py
@time:    2018/4/10 13:15
"""

import os
from functools import wraps
from io import StringIO
from collections import deque
import logging

import matlab.engine
from matlab.engine.matlabengine import MatlabEngine
import attr

from .tools import mat2py, py2mat

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

TEMP_NAME = 'py_temp_'


def execute(func):
    """decorator to execute matlab code from python"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        cmd = func(*args, **kwargs)
        self = args[0]
        self.cmdno += 1
        self.history.append(cmd)

        self.out.truncate(0)
        self.err.truncate(0)
        nargout = kwargs.get('nargout', 0)

        try:
            ret = self.engine.eval(cmd, nargout=nargout, stdout=self.out, stderr=self.err)
        except Exception as e:
            logger.error(e.args[0].strip())
            self.err = e
        else:
            err = self.err.getvalue()
            if err:
                logger.error(f'{err.strip()} with command: "{cmd}"')
            out = self.out.getvalue()
            if out:
                logger.info(out.strip())
            return ret
    return wrapper


@attr.s
class MatPy(object):
    engine = attr.ib(default=None, type=MatlabEngine, repr=False)

    @engine.validator
    def validate_engine(self, attribute, value):
        if not isinstance(value, MatlabEngine):
            self.engine = matlab.engine.connect_matlab()

    verbose: bool = attr.ib(default=True, convert=bool, repr=False)
    history = deque(maxlen=200)
    out = attr.ib(default=StringIO(), init=False, repr=False)
    err = attr.ib(default=StringIO(), init=False, repr=False)
    cmdno: int = attr.ib(default=0, repr=False, init=False)

    path = attr.ib(default=None, repr=False)

    @path.validator
    def validate_path(self, attribute, value):
        # self.addpath_(os.path.dirname(os.path.abspath(__file__)))
        if value is not None:
            self.addpath_(value)

    @execute
    def eval_(self, cmd, **kwargs): return cmd

    def addpath_(self, path):
        try:
            path = path.replace(';', ' ').split()
        except AttributeError:
            path = list(path)

        for p in path:
            self.eval_(f"addpath(genpath('{p}'))")

    @execute
    def clear_(self, *args):
        return 'clear {vars}'.format(vars=' '.join(args))

    @execute
    def save_(self, file_name, *args):
        var_str = ', '.join("'{var}'".format(var=var) for var in args)
        return "save('{file_name}', {var_str})".format(file_name=file_name, var_str=var_str)

    @execute
    def load_(self, file_name):
        return "load('{file_name}');".format(file_name=file_name)

    def py2ws(self, name, value, convert=True):
        if self.engine.exist(name) == 5:
            raise NameError(f"'{name}' is invalid!")
        if convert:
            value = py2mat(value)
        try:
            self.engine.workspace[name] = value
        except ValueError:
            self.engine.workspace[TEMP_NAME] = value
            self.eval_(f'{name} = {TEMP_NAME}; clear {TEMP_NAME};')

    def ws2py(self, name, convert=True):
        try:
            v = self.engine.workspace[name]
        except ValueError:
            self.eval_(f'{TEMP_NAME} = {name};')
            v = self.engine.workspace[TEMP_NAME]
            self.clear_(TEMP_NAME)

        if convert:
            v = mat2py(v)
        return v

    def __del__(self):
        logger.info('Bye!')
        self.engine.exit()

    def __getattr__(self, item):
        """call matlab function"""
        cls = type(self)
        if hasattr(self.engine, item):
            return getattr(self.engine, item)
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, item))
