# -*- encoding: utf-8 -*-
# @File   : _common.py
# @Time   : 2024/01/12 18:54:45
# @Author : Chloride

from os import chdir as setcwd
from sys import path as envpath
envpath.insert(0, envpath[0]+"/../")
setcwd(envpath[0])  # project dir, not script dir

from pyalert2yr import splitMap, joinMap  # noqa: E402, F401
from pyalert2yr.formats import ini, csf  # noqa: E402, F401


def readConfig():
    cfg = ini.INIClass()
    cfg.read('./config.ini')
    return cfg['Settings']
