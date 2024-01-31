# -*- encoding: utf-8 -*-
# @File   : map_packup.py
# @Time   : 2024/01/12 18:23:10
# @Author : Chloride

from os import remove as delete
from shutil import move

from _common import readConfig, yrmap

if __name__ == '__main__':
    yrpycfg = readConfig()
    outpath = str.replace(
        yrpycfg.get('gitutil.mappath', default='./target.map'), '"', '')
    try:
        delete(outpath)
    except Exception:
        pass
    yrmap.joinMap('./src', 'target')
    move('./src/target.map', outpath)
